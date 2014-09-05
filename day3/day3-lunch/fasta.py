"""
This is the module fasta
"""

import sys

# look into genrator might be a better way

#need to keep state while we parse through
class FASTAReader(object):
    def __init__( self , file):              #init initiallizes the state of the object, always pass self as first argument represents the object
        self.file = file
        self.last_sid = None
    def next ( self ):
        if self.last_sid is None:                   #need to know where in the record we are
            line = sys.stdin.readline()
            #assert line.startswith( ">" )           #sanity check, make sure first line begins with a > (assert breaks the code if not True)
            sid = line[1:].rstrip("\r\n")           #cut the > off the id 
        else:
            sid = self.last_sid
            
        sequences = []
        while 1:                                     #this could be while True:
            line=sys.stdin.readline()
            if line == "" and not sequences:        #this says to keep going until we run out of info or sequences
                raise StopIteration                #this tells the caller to stop when it runs out of things to parse
            elif line.startswith( ">" ) or line =="":
                self.last_sid = line[1:].rstrip("\r\n")     #saving on our object the last id that we saw
                break
            else:
                sequences.append( line.strip() )              #get rid of the line breaks

       
        sequence = "".join( sequences)                   #join things using this as a delimiter

        return sid, sequence
        
    def __iter__( self ):
        return self