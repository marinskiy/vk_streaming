
def new_rules(stream):
    # delete current rules
    current_rules = stream.get_rules()
    for rule in current_rules:
        stream.delete_rule(rule['tag'])

    # read new rules from file
    with open('rules_list.txt', 'r') as f:
        rules = f.readlines()

    # add new rules
    count = 0
    for rule in rules:
        count += 1
        tag = 'tag' + str(count)
        rule = rule.strip('\n')
        stream.add_rule(rule, tag)

    # check rules
    current_rules = stream.get_rules()
    for rule in current_rules:
        print(rule)
    print('New rules activated')
    print()
