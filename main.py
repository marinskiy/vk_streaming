# -*- coding: utf-8 -*-
import vk_api
from vk_api.streaming import VkStreaming
from save import *
from set_rules import *


def main():
    # create new session
    vk = vk_api.VkApi(token='<ENTER_YOUR_SERVICE_TOKEN_HERE>')
    streaming = VkStreaming(vk)

    # check if user wants to update rules
    print('Do you want to reset the rules from rules_list.txt? y/n')
    ans = input()
    if ans == 'y':
        new_rules(streaming)

    print('Collecting data...')

    # start listening
    for event in streaming.listen():
        # save only posts
        if event['event_type'] == 'post':
            add_to_db(event)
            tags = '|'.join(event['tags'])
            print('Tags: ' + tags)
            print('Text: ' + event['text'])
            print()


if __name__ == '__main__':
    main()
