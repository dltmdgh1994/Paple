from django.core.exceptions import ValidationError

def validate_pw(value):
    # pw 길이가 4자리 미만, 20자리 초과 이면 validation error
    if (len(value) < 4) | (len(value) > 20):
        msg = "비밀번호는 4자리 이상 20자리 이하로 입력해 주세요."
        raise ValidationError(msg)
