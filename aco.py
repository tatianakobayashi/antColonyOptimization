#import sys

from Application import Application
    
f = open('teste_1.hcp', 'r')

app = Application(f)
#print('App')
app.run()