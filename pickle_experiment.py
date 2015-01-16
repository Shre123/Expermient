
#### Creating the book dictionary

book = {}
 book['title'] = 'Light Science and Magic: An Introduction to Photographic Lighting, Kindle Edition'
 book['page_link'] = 'http://www.amazon.com/Fil-Hunter/e/B001ITTV7A'
 book['comment_link'] = None
 book['id'] = b'\xAC\xE2\xC1\xD7'
 book['tags'] = ('Photography', 'Kindle', 'Light')
 book['published'] = True
 import time> book['published_time'] = time.strptime('Mon Sep 10 23:18:32 2012')
 book['published_time']
time.struct_time(tm_year=2012, tm_mon=9, tm_mday=10, tm_hour=23,
 tm_min=18, tm_sec=32, tm_wday=0, tm_yday=254, tm_isdst=-1
 
 #### Print the just created book dictionary.
 
 print book
 
 #### Creating a pickle file  from book dictionary
 #### 'wb' represnts writng in BInary format.
 
 import pickle
 
 with open('book.pickle', 'wb') as f:
    pickle.dump(book, f)
    
 ####LOading data from apickle file as seenin Udacity ML classes  
  
 b= picle.load(open('book.pickle','r'))
	
 ####Loading data from a pickle file as given website example
 ####MIght be slightly different because the example used teo different Shells to explain
 
 with open('book.pickle','r') as f:
      b =pickle.load(f)
	
	
	
