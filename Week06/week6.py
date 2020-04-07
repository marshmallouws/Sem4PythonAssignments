import os.path
import urllib.request as req
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter


class DownloadBooks:
    # 1
    def __init__(self, url_list, path):
        self.url_list = url_list
        self.path = path

    # 2

    def download(self, url, filename):
        """
        Download url to filename. Raises NotFoundException when url returns 404
        """
        with req.urlopen(url) as response:
            if response.getcode == 404:
                raise NotFoundException
            else:
                data = response.readlines()
                with open(os.path.join(self.path, filename), "wb") as f:
                    f.writelines(data)

    # 3
    def multi_download(self):
        """
        Uses threads to download multiple urls as text and stores filenames as a property
        """
        workers = 5
        with ThreadPoolExecutor(workers) as ex:
            for filename, url in self.url_list.items():
                try:
                    ex.submit(self.download, url, filename)
                    print("I am downloading: ", filename)
                except NotFoundException:
                    print("Oh no! Cannot download", filename)

    # 4
    def __iter__(self):
        """
        Returns iterator
        """
        return iter(self.url_list)

    # 5 -- __iter__ method returns an iterable object each time it is called
    """
    def __next__(self):
        
        Returns next filename and stops when there are no more
        https://stackoverflow.com/questions/38700734/how-to-implement-next-for-a-dictionary-object-to-be-iterable
        
        if not hasattr(self, "_iter"):
            self._iter = iter(self.url_list)
        return next(self._iter)
    """

    # 6
    def urllist_generator(self):
        """
        Returns a generator to loop through the urls
        """
        for filename in self.url_list:
            yield filename

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

        for filename, url in self.url_list.items():
            with open(os.path.join(self.path, filename), "r", encoding="UTF-8") as text:
                texts[filename] = text.read()

        with ProcessPoolExecutor(workers) as p:
            res = zip(texts.keys(), p.map(self.avg_vowels, texts.values()))

        highest = max(res, key=lambda x: x[1])
        return highest[0]

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
