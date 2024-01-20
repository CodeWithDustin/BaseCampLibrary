from dataclasses import dataclass

@dataclass
class Book:
  title: str
  author: str
  synopsis: str
  genre: str
  is_checked_out: bool

bookList = []

ready_player_one = Book("Ready Player One", "Earnest Cline", "The story, set in a dystopia in 2045, follows protagonist Wade Watts on his search for an Easter egg in a worldwide virtual reality game, the discovery of which would lead him to inherit the game creator's fortune.", "science-fiction", False)

leagues_under_the_sea = Book("20000 Leagues Under the Sea", "Jules Verne", "Twenty Thousand Leagues Under the Sea tells the story of three men who go to sea in search of a giant whale. They are taken prisoner on board the world's first submarine – the Nautilus. The Nautilus travels through the world's seas. The men see amazing deep-sea creatures, and they travel to remote islands.", "science-fiction", False)

john_carter = Book("John Carter", "Edgar Rice Burroughs", "The book follows Confederate veteran John Carter after he is suddenly transported from a cave in Arizona to the planet Mars. Carter falls in with a gang of Martians called Tharks, and eventually wins the heart of Heliumite princess Dejah Thoris.", "science-fiction", False)

dune = Book("Dune", "Frank Herbert", "It tells the story of young Paul Atreides, whose family accepts the stewardship of the planet Arrakis. While the planet is an inhospitable and sparsely populated desert wasteland, it is the only source of melange, or 'spice', a drug that extends life and enhances mental abilities.", "science-fiction", False)

enders_game = Book("Ender’s Game", "Orson Scott Card", "The novel tells the story of a young boy, Ender Wiggin, who is sent to a training academy named Battle School, located in orbit above the Earth, built to train people to become soldiers that will one day battle against a vast alien race known as 'Buggers'.", "science-fiction", False)

the_fellowship_of_the_ring = Book("The Fellowship of the Ring", "J.R.R. Tolkien", "Set in Middle-earth during the Third Age, The Fellowship of the Ring follows the unlikely hero, Frodo Baggins, in his quest to destroy the One Ring of ultimate power before the evil Sauron can regain the weapon.", "fantasy", False)

the_way_of_kings = Book("The Way of Kings", "Brandon Sanderson", "Kaladin, a slave who has ended up a soldier in Amaram's army. Kaladin struggles with where his life has ended up and the horrific life of a bridgecrewman – the most junior soldier in any army – but is determined to improve things for both himself and his crew, Bridge Four.", "fantasy", False)

the_once_and_future_king = Book("The Once and Future King", "T. H. White", "The Once and Future King tells the story of the title character King Arthur from his birth until his death. In The Sword in the Stone, Arthur is known by the nickname Wart. He learns from the wizard Merlyn how to rule, and each of these lessons follows him throughout the rest of his rule.", "fantasy", False)

american_gods = Book("American Gods", "Neil Gaiman", "At face value it's a fantasy story about a war between the old gods (Odin, Anansi, Bilquis, Czernobog, and fantastical beings like leprechauns) who were brought over by immigrants who believed in them and the new gods (technology, media, small town America, the open road) that our society has replaced them with.", "fantasy", False)

the_invisible_life_of_addie_larue = Book("The Invisible Life of Addie LaRue", "V.E. Schwab", "The story follows a young French woman in 1714 who makes a bargain with the Dark that makes her immortal, but curses her to be forgotten by everyone she meets.", "fantasy", False)

essays = Book("Essays", "Michel de Montaigne", "Essays is the title given to a collection of 107 essays written by Michel de Montaigne that was first published in 1580. Montaigne essentially invented the literary form of essay, a short subjective treatment of a given topic, of which the book contains a large number. Essai is French for 'trial' or 'ttempt'.", "non-fiction", False)

walden = Book("Walden", "Henry David Thoreau", "Walden (first published as Walden; or, Life in the Woods) is an American book written by noted transcendentalist Henry David Thoreau, a reflection upon simple living in natural surroundings.", "non-fiction", False)

confessions = Book("Confessions", "Augustine", "Confessions is the name of an autobiographical work, consisting of 13 books, by St. Augustine of Hippo, written between AD 397 and AD 398. Modern English translations of it are sometimes published under the title The Confessions of St. Augustine in order to distinguish the book from other books with similar titles, such as Jean-Jacques Rousseau's Confessions.", "non-fiction", False)

the_interpretation_of_dreams = Book("The Interpretation of Dreams", "Sigmund Freud", "This book introduces Freud's theory of the unconscious with respect to dream interpretation. Dreams, in Freud's view, were all forms of 'wish-fulfillment' — attempts by the unconscious to resolve a conflict of some sort, whether something recent or something from the recesses of the past (later in Beyond the Pleasure Principle, Freud would discuss dreams which did not appear to be wish-fulfillment). However, because the information in the unconscious is in an unruly and often disturbing form, a 'censor' in the preconscious will not allow it to pass unaltered into the conscious. During dreams, the preconscious is more lax in this duty than in waking hours, but is still attentive: as such, the unconscious must distort and warp the meaning of its information to make it through the censorship. As such, images in dreams are often not what they appear to be, according to Freud, and need deeper interpretation if they are to inform on the structures of the unconscious.", "non-fiction", False)

the_prince = Book("The Prince", "Niccolo Machiavelli", "Il Principe (The Prince) is a political treatise by the Florentine public servant and political theorist Niccolò Machiavelli. Originally called De Principatibus (About Principalities), it was originally written in 1513, but not published until 1532, five years after Machiavelli's death. The treatise is not representative of the work published during his lifetime, but it is the most remembered, and the work responsible for bringing 'Machiavellian' into wide usage as a pejorative term.", "non-fiction", False)

the_haunting_of_hill_house = Book("The Haunting of Hill House", "Shirley Jackson","Dr. Montague decides it's time science proved the existence of the supernatural and that Hill House, a mansion with a pretty haunted history, is the place to prove it. His experiment will only consist of the most rigorous science and indisputable evidence.", "horror", False)

it = Book("It", "Stephen King", "The story begins when a band of seven “uncool” 11-year-olds, led by Bill Denbrough, discovers and battles an evil, shape-changing monster that the children call “It.” It attacks every 27 years, taking on a variety of terrifying guises—predominantly that of the clown Pennywise—and committing appalling acts.", "horror", False)

tales = Book("Tales", "H. P. Lovecraft", "Set in a meticulously wrought, historically grounded New England landscape, his harrowing stories explore the collapse of sanity beneath the weight of chaotic events. Lovecraft's universe is a frightening shadow world were reality and nightmare intertwine, and redemption can come only from below.", "horror", False)

books_of_blood = Book("Books of Blood", "Clive Barker", "Books of Blood is a series of six horror fiction anthologies collecting original stories written by British author, playwright, and filmmaker Clive Barker in 1984 and 1985. Known primarily for writing stage plays beforehand, Barker gained a wider audience and fanbase through this anthology series, leading to a successful career as a novelist. Originally presented as six volumes, the anthologies were subsequently re-published in two omnibus editions containing three volumes each. Each volume contains four, five or six stories. ", "horror", False)

the_cipher = Book("The Cipher", "Kathe Koja", "This is about Nicholas and Nakota who find a hole in a storage room in Nicholas's apartment building. When they lower things into the hole they come out transformed. Initial curiosity develops into full-blown obsession and the story becomes incredibly unsettling and psychologically horrific.", "horror", False)

def getBookList():
  bookList.append(ready_player_one)
  bookList.append(leagues_under_the_sea)
  bookList.append(john_carter)
  bookList.append(dune)
  bookList.append(enders_game)
  bookList.append(the_fellowship_of_the_ring)
  bookList.append(the_way_of_kings)
  bookList.append(the_once_and_future_king)
  bookList.append(american_gods)
  bookList.append(the_invisible_life_of_addie_larue)
  bookList.append(essays)
  bookList.append(walden)
  bookList.append(confessions)
  bookList.append(the_interpretation_of_dreams)
  bookList.append(the_prince)
  bookList.append(the_haunting_of_hill_house)
  bookList.append(it)
  bookList.append(tales)
  bookList.append(books_of_blood)
  bookList.append(the_cipher)
  
  return bookList
