class Text:

    def __init__(self, csv_address, color_word_map_dict, output_address):

        self.csv_address = csv_address
        self.output_address = output_address
        self.color_word_map_dict = color_word_map_dict
        self.csv_file = ''
        self.text_dict = []
        self.csv_header = ''

    def csv_opener(self):

        self.csv_file = open(self.csv_address, 'r')
        self.csv_header = self.csv_file.readline().split()[1:]

    def output_file_maker(self):
        output = open(self.output_address, 'a+')
        output.write(str(self.text_dict) + '\n')
        output.close()

    def text_maker(self , make_file=True):
        self.text_dict = []
        self.csv_opener()
        for line in self.csv_file:
            records = line.split(',')
            #break_flag = False
            #records = split_line.split(',')
            if len(records) > 0:
                word = records[1].strip()
                tags = records[4:]
                tags = tags[1::2]
                tag_label = []
                for t in tags:
                    t = t.strip()
                    if t != 'o' and t not in tag_label :
                        tag_label.append(t.strip())
                tag_label = ','.join(tag_label)
                if word != '':
                    if word == '.':
                        self.text_dict.append({word + '\n':0})
                    elif tag_label in self.color_word_map_dict:
                        self.text_dict.append({word:self.color_word_map_dict[tag_label]})
                    else:
                        self.text_dict.append({word:0})
            # for word in self.color_word_map_dict:
            #     if len(word.split(',')) != 1:
            #         multiple_word_flag = False
            #         for single_word in word.split(','):
            #             if single_word not in split_line:
            #                 multiple_word_flag = True
            #                 break
            #         if not multiple_word_flag:
            #             self.text_dict[split_line[0]] = self.color_word_map_dict[word]
            #             break_flag = True

            # if not break_flag:
            #     for word in self.color_word_map_dict:
            #         if len(word.split(',')) == 1 and word in split_line:
            #             self.text_dict[split_line[0]] = self.color_word_map_dict[word]
            #             break_flag = True
            # if not break_flag:
            #     if split_line[0] == '.':
            #         self.text_dict['. \n'] = ''
            #     else:
            #         self.text_dict[split_line[0]] = '0'
            if make_file:
                self.output_file_maker()
                self.text_dict = {}
