class Text:

    def __init__(self, csv_address, color_word_map_dict, output_address):

        self.csv_address = csv_address
        self.output_address = output_address
        self.color_word_map_dict = color_word_map_dict
        self.csv_file = ''
        self.text_dict = []
        self.csv_header = ''
        self.repeated_words = dict()

    def csv_opener(self):

        self.csv_file = open(self.csv_address, 'r')
        self.csv_header = self.csv_file.readline().split()[1:]

    def output_file_maker(self):
        output = open(self.output_address, 'a+')
        for i in self.text_dict:

            output.write(str(i) + '\n')
        output.close()

    def text_maker(self, make_file=True):
        self.repeated_words = dict()
        for word in self.color_word_map_dict:
            self.repeated_words[word] = 0
        colors = []
        color_words = []
        self.text_dict = []
        self.csv_opener()
        temp_list = []
        for line in self.csv_file:
            records = line.split(',')

            if len(records) > 0:
                word = records[1].strip()
                tags = records[4:]
                tags = tags[1::2]
                tag_label = []
                for t in tags:
                    t = t.strip()
                    if t != 'o' and t not in tag_label:
                        tag_label.append(t.strip())
                tag_label = ','.join(tag_label)
                if word != '':
                    if word == '.':
                        self.text_dict.append({word + '\n': 0})
                    elif tag_label in self.color_word_map_dict:
                        color_words.append(word)
                        colors.append(self.color_word_map_dict[tag_label])

                        if len(colors) > 1 and self.color_word_map_dict[tag_label] == colors[-2]:
                            if not temp_list and len(color_words) > 1:
                                temp_list.append({color_words[-2]: colors[-2]})
                                self.repeated_words[tag_label] += 1
                            temp_list.append({word: self.color_word_map_dict[tag_label]})
                            self.repeated_words[tag_label] += 1
                        elif temp_list:
                            print(temp_list)
                            statement = ""
                            for single_word in temp_list:
                                statement += str(*single_word.keys()) + " "
                            self.text_dict.append({
                                statement: self.color_word_map_dict[tag_label], 'tag_label': tag_label
                            })
                            temp_list = []
                            if make_file:
                                self.output_file_maker()
                                self.text_dict = []
                            self.text_dict.append({word: self.color_word_map_dict[tag_label], 'tag_label': tag_label})
                            self.repeated_words[tag_label] += 1

                        else:
                            self.text_dict.append({word: self.color_word_map_dict[tag_label], "tag_label": tag_label})
                            self.repeated_words[tag_label] += 1

                    else:
                        self.text_dict.append({word: 0})

            if make_file:
                self.output_file_maker()
                self.text_dict = []
