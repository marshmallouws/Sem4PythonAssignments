import week6

if __name__ == "__main__":

    urls = {
        "The_Importance_of_Being_Earnest.txt": "https://www.gutenberg.org/ebooks/844.txt.utf-8",
        "Grimms_Fairy_Tales.txt": "https://www.gutenberg.org/files/2591/2591-0.txt",
        "The_Call_of_the_Wild.txt": "https://www.gutenberg.org/files/215/215-0.txt",
        "Ion.txt": "https://www.gutenberg.org/ebooks/1635.txt.utf-8",
        "A_Modest_Proposal.txt": "https://www.gutenberg.org/files/1080/1080-0.txt",
        "A_Tale_of_Two_Cities.txt": "https://www.gutenberg.org/files/98/98-0.txt",
        "War_and_Peace.txt": "https://www.gutenberg.org/files/2600/2600-0.txt",
        "A_Christmas_Carol.txt": "https://www.gutenberg.org/files/46/46-0.txt",
        "A_Dolls_House.txt": "https://www.gutenberg.org/ebooks/2542.txt.utf-8",
        "The_Adventures_of_Tom_Sawyer.txt": "https://www.gutenberg.org/files/74/74-0.txt",
    }
    b = week6.DownloadBooks(urls)
    # b.multi_download()
    c = iter(b)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
