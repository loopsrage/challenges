from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def perform_search(driver, **kwargs):
    """
    Finds the search element on the page
    Performs a search
    """
    # Required parameters
    search = kwargs['search']
    selector = kwargs['selector']

    # Parameters with defaults
    by_type = By.ID
    return_allowed = True

    # Set by_type to kwarg value if provided
    if 'by_type' in kwargs:
        by_type = kwargs['by_type']

    # Use provided value for return_allowed
    if 'return_allowed' in kwargs:
        return_allowed = kwargs['return_allowed']

    # If return is allowed, append ENTER key to end of search term
    if return_allowed:
        search = "{}{}".format(search, Keys.ENTER)

    # Locate the element
    search_elem = driver.find_element(by_type, selector)

    # Clear any current data
    search_elem.clear()

    # Send the search term
    search_elem.send_keys(search)


def find_elements_of_type(driver, **kwargs):
    """
    Using a selector find all instances of the element on the page
    """
    # Required parameters
    selector = kwargs['selector']

    # Parameters with defaults
    only_count = False
    by_type = By.XPATH
    if 'only_count' in kwargs:
        only_count = kwargs['only_count']

    if 'by_type' in kwargs:
        by_type = kwargs['by_type']

    results = driver.find_elements(by_type, selector)

    if only_count:
        return len(results)
    else:
        return results


def sort_strings(list_of_strings):
    """
    Group strings of like type together
    """
    result_obj = {}
    for i in list_of_strings:
        if i in result_obj:
            result_obj[i] = result_obj[i] + 1
        else:
            result_obj[i] = 1

    return result_obj

