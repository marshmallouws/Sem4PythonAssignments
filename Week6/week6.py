import os.path
import urllib.request as req
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter


class Download_Books:
    # 1
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []
        self.idx = 0

    # 2
    def download(self, url, filename):
        """
        Download url to filename. Raises NotFoundException when url returns 404
        """
        try:
            with req.urlopen(url) as response:
                data = response.readlines()
        except:
            raise NotFoundException
        else:
            filename = os.path.basename(url)
            with open(filename, "wb") as f:
                f.writelines(data)

    # 3
    def multi_download(self, urls):
        """
        Uses threads to download multiple urls as text and stores filenames as a property
        """
        workers = 5
        with ThreadPoolExecutor(workers) as ex:
            for u in urls:
                filename = os.path.basename(u)
                try:
                    ex.submit(self.download, u, filename)
                except NotFoundException:
                    pass
                else:
                    self.filenames.append(filename)

    # 4
    def __iter__(self):
        """
        Returns iterator
        """
        return self

    # 5
    def __next__(self):
        """
        Returns next filename and stops when there are no more)
        """
        if self.idx < len(self.filenames):
            idx = self.idx
            self.idx += 1
            return self.filenames[idx]
        else:
            self.idx = 0
            raise StopIteration

    # 6
    def urllist_generator(self):
        """
        Returns a generator to loop through the urls
        """
        idx = 0
        while idx <= len(self.url_list):
            yield self.url_list[idx]
            idx += 1

    # 7
    def avg_vowels(self, text):
        """
        A rough estimate on readability returns average number of vowels in the words of the text
        """
        words = text.split()
        letters = Counter(text.lower())
        no_of_vowels = sum(
            v for k, v in letters.items() if k in ["a", "e", "i", "o", "u", "y"]
        )

        return no_of_vowels / len(words)

    def hardest_read(self):
        """
        Returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.)
        """
        workers = multiprocessing.cpu_count()

        texts = {}

        for f in self.filenames:
            with open(f, "r", encoding="UTF-8") as text:
                texts[f] = text.read()

        with ProcessPoolExecutor(workers) as p:
            res = zip(texts.keys(), p.map(self.avg_vowels, texts.values()))

        highest = 0
        f = ""
        for filename, avg in res:
            if avg > highest:
                highest = avg
                f = filename
        return f

    def multi_download1(self, urls):
        """
        Uses threads to download multiple urls as text and stores filenames as a property
        """
        workers = 5
        with ThreadPoolExecutor(workers) as ex:
            for u in urls:
                filename = os.path.basename(u)
                try:
                    ex.submit(self.download, u, filename)
                except NotFoundException:
                    pass
                else:
                    self.filenames.append(filename)


class NotFoundException(Exception):
    pass


if __name__ == "__main__":
    b = Download_Books([])
    b.multi_download(
        [
            "https://www.gutenberg.org/files/84/84-0.txt",
            "https://www.gutenberg.org/files/43/43-0.txt",
        ]
    )
    print(b.hardest_read())
