from pycraft import parsematerial


def test_parse():
    for text, expected in [
        ('air', {'namespace': 'minecraft', 'name': 'air', 'properties': {}}),
        ('minecraft:air', {'namespace': 'minecraft', 'name': 'air', 'properties': {}}),
        (
            'minecraft:smooth_quartz',
            {'namespace': 'minecraft', 'name': 'smooth_quartz', 'properties': {}},
        ),
        (
            'minecraft:smooth_quartz_stairs[facing=west,half=bottom,shape=straight,waterlogged=false]',
            {
                'namespace': 'minecraft',
                'name': 'smooth_quartz_stairs',
                'properties': {
                    'facing': 'west',
                    'half': 'bottom',
                    'shape': 'straight',
                    'waterlogged': 'false',
                },
            },
        ),
    ]:
        result = parsematerial.parse_material(text)
        assert (
            result == expected
        ), f"Parse Failed on {text}\n  got {result}\n  expected {expected}"


def test_unparse():
    for material, expected in [
        ({'namespace': 'minecraft', 'name': 'air', 'properties': {}}, 'minecraft:air'),
        (
            {
                'namespace': 'minecraft',
                'name': 'smooth_quartz_stairs',
                'properties': {
                    'facing': 'west',
                    'half': 'bottom',
                    'shape': 'straight',
                    'waterlogged': 'false',
                },
            },
            'minecraft:smooth_quartz_stairs[facing=west,half=bottom,shape=straight,waterlogged=false]',
        ),
    ]:
        result = parsematerial.unparse_material(material)
        assert (
            result == expected
        ), f"Unparse Failed on {material}\n got {result}\n  expected {expected}"
