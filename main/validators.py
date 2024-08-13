from django.core.exceptions import ValidationError


def check_the_csv(value):
    """
    this function check that we should enter the csv file only and we don't enter another files
    Args:
        value (_type_): csv file
    """
    if not value.name.endswith('.csv'):
        raise ValidationError('Only csv files are allowed')