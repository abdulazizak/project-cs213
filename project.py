#abdulaziz khalid alawad id 391108573
import csv
# Group Class
class Group:
	def __init__(self):
		self.__Members = list()

	def addMember(self, member):
		self.__Members.append(member)

	def groupNumber(self):
		return len(self.__Members)

	def listGroup(self):
		return (self.__Members)

	def getMember(self, member):
		return self.__Members[member]

# File Class
class File:
	group = Group()

	def __init__(self, fileName):
		self.__fileName = fileName
		self.__group = Group()
		file = open(fileName, 'r')
		self.readFile(fileName)

	def readFile(self, file):
		n = -1
		with open(file, 'r') as csvFile:
			readCSV = csv.reader(csvFile, delimiter=',')
			for line in readCSV:
				if (line[0][:6] == "Member"):
					name: str = line[1]
					phone = line[2]
					mail = line[3]
					member = Member(name, phone, mail)
					self.group.addMember(member)
					n = n + 1
				elif (line[0][:4] == "Book"):
					title = line[1]
					pages = line[2]
					category = line[3]
					book = Book(title, pages, category)
					self.group.getMember(n).addBook(book)


# Member Class
class Member:
	def __init__(self, Name, Mobile, Email):
		self.__Name = Name
		self.__Mobile = Mobile
		self.__Email = Email
		self.__TotalBooks = 0
		self.__Books = list()

	def listBooks(self):
		return (self.__Books)

	def addBook(self, book):
		self.__Books.append(book)
		self.__TotalBooks = self.__TotalBooks + 1

	def getName(self):
		return self.__Name

	def getMobile(self):
		return self.__Mobile

	def getEmail(self):
		return self.__Email

	def getTotalBooks(self):
		return self.__TotalBooks

	def getTotalPages(self):
		sum = 0
		for book in self.listBooks():
			sum = sum + book.getPages()
		return sum

# Book Class
class Book:
	def __init__(self, Title, Pages, Category):
		self.__Title = Title
		self.__Pages = Pages
		self.__Category = Category

	def getTitle(self):
		return self.__Title

	def getPages(self):
		return int(self.__Pages)

	def getCategory(self):
		return self.__Category

# Rank Class

class Ranking:

	def __init__(self, file):
		self.__group = file.group.listGroup()

	def totalBooks(self):
		sum = 0
		for member in self.__group:
			sum = sum + member.getTotalBooks()
		print("Total number of books is", sum, "Books\n")

	def totalPages(self):
		sum = 0
		for member in self.__group:
			sum = sum + member.getTotalPages()
		print("Total number of pages is", sum, "Pages\n")

	def __bubbleSort(self, array_1, array_2):
		n = len(array_1)
		for i in range(n - 1):
			for j in range(0, n - i - 1):
				if array_1[j] < array_1[j + 1]:
					array_1[j], array_1[j + 1] = array_1[j + 1], array_1[j]
					array_2[j], array_2[j + 1] = array_2[j + 1], array_2[j]

	def categoryRank(self):
		rank = list()
		category = list()
		for member in self.__group:
			for book in member.listBooks():
				if (book.getCategory() in category):
					indx = category.index(book.getCategory())
					rank[indx] = rank[indx] + 1
				else:
					category.append(book.getCategory())
					rank.append(1)

		self.__bubbleSort(rank, category)
		x = 1
		for i in category:
			print(x, "-", i, "Category, It has been read ", rank[category.index(i)],"Times", "\n")
			x = x + 1

	def booksRank(self):
		members = list()
		booksNumbers = list()
		for member in self.__group:
			members.append(member.getName())
			booksNumbers.append(member.getTotalBooks())

		self.__bubbleSort(booksNumbers, members)
		x = 1
		for member in members:
			print(x, "-", member, "has read", booksNumbers[members.index(member)], "Books\n")
			x = x + 1

	def pagesRank(self):
		members = list()
		pages = list()
		for member in self.__group:
			members.append(member.getName())
			pages.append(member.getTotalPages())

		self.__bubbleSort(pages, members)
		x = 1
		for member in members:
			print(x, "-", member, "has read", pages[members.index(member)], "Pages\n")
			x = x + 1


f = File("inputFile.txt")
s = Ranking(f)
while True:
	l = int(input(
		"Enter\n 1 to show Total books the group has read\n 2 to show The total number of pages the group read \n 3 to ranking Most read categories\n 4 to show who the most read books and how many  \n 5 to show who the most read pages and how many\n or -1 to terminat the program"))
	print(
		"-----------------------------------------------------------------------------------------------------------------------")
	if l == 1:
		s.totalBooks()
		print("___________________________________________________________")
	elif l == 2:
		s.totalPages()
		print("___________________________________________________________")
	elif l == 3:
		s.categoryRank()
		print("___________________________________________________________")
	elif l == 4:
		s.booksRank()
		print("___________________________________________________________")
	elif l == 5:
		s.pagesRank()
		print("___________________________________________________________")
	elif l == -1:
		print("you have terminated the program thank you")
		print("___________________________________________________________")
		break

