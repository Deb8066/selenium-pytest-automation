class FormTestData:

    VALID_NAME = "Test Name"
    VALID_EMAIL = "testemail@xyz.com"
    VALID_PHONE = "2244567890"
    DOB = "05/25/1987"
    START_DATE = "03/25/2026"
    END_DATE = "04/21/2026"
    COUNTRY = "India"
    COLOR = "Blue"
    EXPECTED_RESULT = "You selected a range of 27 days."

    # Parameterized data set
    USERS = [
        ("Alice", "alice@test.com", "9876543210"),
        ("Bob", "bob@test.com", "8765432109"),
        ("Charlie", "charlie@test.com", "7654321098"),
    ]

