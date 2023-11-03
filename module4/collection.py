# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = ["Charles Dickens, William Thackeray, Anthony Trollope, Gerard Manley Hopkins"]
dates = ["1870, 1863, 1882, 1889"]

   # "Charles Dickens": "1870",
 #   "William Thackeray": "1863",
 #   "Anthony Trollope": "1882",
  #  "Gerard Manley Hopkins": "1889"

for dates in authors:
    print("%s" % authors + " died in " + " % dates")