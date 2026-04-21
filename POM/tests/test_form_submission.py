import pytest

from POM.pages.form_page import FormPage
from POM.testdata.form_test_data import FormTestData as Data


@pytest.mark.parametrize("name,email,phone",Data.USERS)
@pytest.mark.regression
@pytest.mark.smoke
def test_form_submission(driver):
    form = FormPage(driver)

    form.enter_personal_details(
        Data.VALID_NAME, Data.VALID_EMAIL, Data.VALID_PHONE
    )
    form.select_gender_and_day()
    form.select_country_and_color(Data.COUNTRY, Data.COLOR)
    form.enter_dates(Data.DOB, Data.START_DATE, Data.END_DATE)
    form.submit_form()

    assert Data.EXPECTED_RESULT in form.get_result_message()