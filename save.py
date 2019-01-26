import pandas as pd
from datetime import timedelta


def add_to_db(message):

    df = pd.DataFrame(columns=['event_type',
                               'event_id',
                               'event_url',
                               'text',
                               'action',
                               'action_time',
                               'creation_time',
                               'attachments',
                               'geo',
                               'shared_post_text',
                               'shared_post_creation_time',
                               'signer_id',
                               'tags',
                               'author'])

    # create dataframe with null values
    for column in df.columns:
        df[column] = [None]

    # fill dataframe with available information
    for element, value in message.items():
        df.at[0, element] = value

    # change time formatting
    time = pd.to_datetime(df['creation_time'][0], unit='s') + timedelta(hours=3)
    df.at[0, 'creation_time'] = time

    # write to file
    with open(get_file_name(time), 'a', encoding="utf-8") as f:
        df.to_csv(f, header=False, index=False)


def get_file_name(time):
    # create filename from timestamp
    filename = str(time.year) + '_' + \
               str(time.month) + ' ' + \
               str(time.day) + '_' + \
               str(time.hour) + '.csv'
    return filename
