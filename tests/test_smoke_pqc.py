"""Smoke-тест: установленная cryptography умеет ML-KEM и ML-DSA.

Если эти тесты падают, в окружении слишком старая cryptography (до 48)
или сборка без поддержки постквантовых алгоритмов. Остальной проект на них опирается.
"""

import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import mldsa, mlkem


def test_mlkem768_shared_secret_matches():
    private_key = mlkem.MLKEM768PrivateKey.generate()
    public_key = private_key.public_key()

    # Отправитель «запечатывает» случайный секрет открытым ключом получателя
    shared_secret, ciphertext = public_key.encapsulate()

    # Получатель «распечатывает» шифртекст закрытым ключом и получает тот же секрет
    assert private_key.decapsulate(ciphertext) == shared_secret
    assert len(shared_secret) == 32
    assert len(ciphertext) == 1088


def test_mldsa65_signature_verifies():
    private_key = mldsa.MLDSA65PrivateKey.generate()
    message = b"pqc-scout smoke test"

    signature = private_key.sign(message)

    # verify ничего не возвращает: если подпись не сходится, он бросает InvalidSignature
    private_key.public_key().verify(signature, message)
    assert len(signature) == 3309


def test_mldsa65_rejects_tampered_message():
    private_key = mldsa.MLDSA65PrivateKey.generate()
    signature = private_key.sign(b"original message")

    with pytest.raises(InvalidSignature):
        private_key.public_key().verify(signature, b"tampered message")
