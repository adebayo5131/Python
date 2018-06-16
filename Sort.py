class Sort():
    list = [2, 5, 3, 4, 1]


    def sort_asending(self):
        # if self.list == []:
        #     raise Exception("List is empty")
        for i in range(len(self.list)):
            for j in range(0, len(self.list)-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]

        return self.list



    def sort_descending(self):

        if self.list == []:
            raise Exception("List is empty")
        for i in range(len(self.list)):
            for j in range(0, len(self.list) - i - 1):
                if self.list[j] < self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]

        return self.list


    def printer(self):
        print(self.sort_asending())
        print(self.sort_descending())

if __name__ =='__main__':
    Sort().printer()
