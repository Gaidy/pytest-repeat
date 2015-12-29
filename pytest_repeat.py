from _pytest.mark import KeywordMapping


def match_keyword(keywordexpr, mapped_names):
    # Monkeyed from _pytest/mark.py
    if keywordexpr == "*":
        return True
    mapping = KeywordMapping(mapped_names)
    if " " not in keywordexpr:
        # special case to allow for simple "-k pass" and "-k 1.3"
        return mapping[keywordexpr]
    elif keywordexpr.startswith("not ") and " " not in keywordexpr[4:]:
        return not mapping[keywordexpr[4:]]
    return eval(keywordexpr, {}, mapping)


def pytest_addoption(parser):
    """
    :type parser: _pytest.config.Parser
    """
    g = parser.getgroup('Repeat')
    g.addoption(
        '--repeat', action='append', dest='repeat_specs',
        help='Number of times to repeat tests '
             'matching the given filter (like `-k`). E.g. `foo:10`'
    )


def pytest_configure(config):
    repeats = []
    for repeat_spec in (config.option.repeat_specs or ()):
        kw, count = repeat_spec.rsplit(":", 1)
        count = int(count)
        if count > 1:
            repeats.append((kw, count))
    config.option.repeat_specs = repeats


def pytest_generate_tests(metafunc):
    for kw, count in metafunc.config.option.repeat_specs:
        if match_keyword(kw, (metafunc.function.__name__,)):
            metafunc.fixturenames.append('_repeat_count')
            metafunc.parametrize('_repeat_count', list(range(count)))
