from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "fabrici01"
    invalid_key = "fabricio"
    invalid_message = 123
    with pytest.raises(TypeError, match="Invalid type for key"):
        encrypt_message(message, invalid_key)

    with pytest.raises(TypeError, match="Invalid type for message"):
        encrypt_message(invalid_message, 123)


# Duvidas tirar na mentoria
