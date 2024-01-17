from bayesian_net import BayesianNet

T, F = True, False


def build_network():
    bn = BayesianNet([
        ('VA', '', 0.09),
        ('MP', '', 0.09),
        ('SI', 'MP', {T: 0.6, F: 0.2}),
        ('RE', 'VA', {T: 0.75, F: 0.6}),
        ('HA', 'RE SI', {(T, T): 0.87, (T, F): 0.8, (F, T): 0.5, (F, F): 0.1}),
        ('DA', 'MP', {T: 0.3, F: 0.05})
    ])
    # TODO: build network that is provided for you on Moodle: A5 Exact Inference, include probability distributions

    return bn


if __name__ == '__main__':
    bn = build_network()
    # optional: visualize network to check whether the structure is correct

    # TODO: compute the answers to the probabilistic queries (provided on Moodle A5 Exact Inference)
    # TODO: print results
    # TODO: enter required numbers in Moodle
    # Hint: use bn.event_probability(event)
    #1. The value of alpha for P(SI | mp, va, re, ha)
    alpha = bn.event_probability({'MP': T, 'VA': T, 'RE': T, 'HA': T})
    print('alpha =', round(alpha, 5))

    #2. The value for P(mp, si, ha, va, re)
    p_2 = bn.event_probability({'MP': T, 'SI': T, 'HA': T, 'VA': T, 'RE': T})
    print('P(mp, si, ha, va, re) =', round(p_2, 5))

    #3. The value for P(mp, ¬ si, ha, va, re)
    p_3 = bn.event_probability({'MP': T, 'SI': F, 'HA': T, 'VA': T, 'RE': T})
    print('P(mp, ¬ si, ha, va, re) =', round(p_3, 5))

    #4. The value for P(si | mp, va, re, ha)
    p_4 = bn.event_probability({'MP': T, 'VA': T, 'RE': T, 'HA': T, 'SI': T}) / bn.event_probability({'MP': T, 'VA': T, 'RE': T, 'HA': T})
    print('P(si | mp, va, re, ha) =', round(p_4, 5))

    #5. The value for P(¬ si | mp, va, re, ha)
    p_5 = bn.event_probability({'MP': T, 'VA': T, 'RE': T, 'HA': T, 'SI': F}) / bn.event_probability({'MP': T, 'VA': T, 'RE': T, 'HA': T})
    print('P(¬ si | mp, va, re, ha) =', round(p_5, 5))


