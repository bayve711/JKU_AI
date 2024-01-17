from bayesian_net import BayesianNet

bn = BayesianNet([
    ('Mane', ''),
    ('Sleep', ''),
    ('Competitors', ''),
    ('Rewards', ''),
    ('Speed', 'Sleep'),
    ('Racing', 'Speed Competitors Rewards')
])


# TODO: visualize the result
# TODO: include your first name and matriculation number in the title
bn.draw('Daniil k12149099', save_path='Graph')


