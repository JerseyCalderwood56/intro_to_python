data = [['1', '2020-12-30', 'kevin@example.com', 'mary@example.com', 'Demo', 'Now is the time...', 'mail_source1.csv'],
        ['2', '2020-12-30', 'kevin@example.com', 'mary@example.com', 'Demo', 'Now is the time...', 'mail_source1.csv'],
        ['3', '2020-12-29', 'bob@example.com', 'mary@example.com', 'Demo', 'Now is the time...', 'mail_source1.csv'],
        ['4', '2020-12-29', 'bob@example.com', 'mary@example.com', 'Demo', 'Now is the time...', 'mail_source1.csv'],
        ['5', '2020-12-29', 'info@example.com', 'mary@example.com', 'Demo', 'Now is the time...', 'mail_source1.csv'],
        ['1', '2020-12-30', 'kevin@example.com', 'joe@example.com', 'Demo', 'Now is the time...', 'mail_source2.csv'],
        ['2', '2020-12-30', 'kevin@example.com', 'joe@example.com', 'Demo', 'Now is the time...', 'mail_source2.csv'],
        ['3', '2020-12-28', 'bob@example.com', 'joe@example.com', 'Demo', 'Now is the time...', 'mail_source2.csv'],
        ['4', '2020-12-28', 'sales@example.com', 'joe@example.com', 'Demo', 'Now is the time...', 'mail_source2.csv'],
        ['5', '2020-12-29', 'bob@example.com', 'joe@example.com', 'Demo', 'Now is the time...', 'mail_source2.csv'],
        ['1', '2020-12-30', 'kevin@example.com', 'alice@example.com', 'Demo', 'Now is the time...', 'data'],
        ['2', '2020-12-30', 'kevin@example.com', 'alice@example.com', 'Demo', 'Now is the time...', 'data'],
        ['3', '2020-12-29', 'bob@example.com', 'alice@example.com', 'Demo', 'Now is the time...', 'data'],
        ['4', '2020-12-29', 'bob@example.com', 'alice@example.com', 'Demo', 'Now is the time...', 'data'],
        ['5', '2020-12-29', 'info@example.com', 'alice@example.com', 'Demo', 'Now is the time...', 'data']]

FROM_INDEX = 2


def summarize(data, column_index):
    summary = {}
    for row in data:
        value = row[FROM_INDEX]
        if value not in summary:
            summary[value] = 1
        else:
            summary[value] += 1
    return summary

COLUMN_INDEX = 2  # FROM EMAIL
print(summarize)
