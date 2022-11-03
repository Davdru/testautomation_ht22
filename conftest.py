import pytest



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.failed:
            # report.nodeid är namnet på testet på formen pythonfil::testfunktion
            filename = f"screenshots/{report.nodeid.replace('::', '__').replace('.py', '_')}.png"
            report_path = "reports/" # TODO styr var bilderna sparas beroende på argumenten till pytest --html=
            browser = item.funcargs['browser']

            browser.save_screenshot(report_path + filename)
            extra.append(pytest_html.extras.html(create_img_tag(filename)))

        report.extra = extra


def create_img_tag(file_path):
    return f'<div class="image"><a href="{file_path}"><img src="{file_path}"/></a></div>'

# TODO vi vill kanske ha en ny rapportkatalog per körning