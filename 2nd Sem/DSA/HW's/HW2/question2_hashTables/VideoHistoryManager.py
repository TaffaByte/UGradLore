from VideoHistoryHashTable import *
import csv
#Takes in list of Dictionaries in format[{},{}] 
# Returns HashTable in the Format [{'ID':..,"DATA":{}}]
def create_VideoHistory(VideoRecords):
    size=7
    pass
    
        
    
    
#Takes as input the Hashtable and Name of Operation file 
# Returns a Tuple with two items 
#   1. collision Path in the format {1:[],2:[]} where the keys are the Operation number
#   2. Final HashTable After All Operations performed.
def perform_Operations(H,operationFile):

    pass

            

            
#Takes the File name is input 
# Returns the list of Dictionaries to be converted to a hashtable in format [{},{}...]
def main(filename):
    hmap = {'Video_ID': 0, 'Video_URL': 1, 'Views': 2, 'Likes': 3, 'Dislikes': 4}
    vid_dict = {}
    with open(filename, 'r') as file:
        data = csv.read_csv(file)
        data.columns = hmap.keys()
        for _, row in data.iterrows():
            vid_dict[row['Video_ID']] = {
                'Video_URL': row['Video_URL'],
                'Views': row['Views'],
                'Likes': row['Likes'],
                'Dislikes': row['Dislikes']
            }
        print(vid_dict)

# Driver Code
VideoRecords=main('watchedVideos.csv')
print(VideoRecords)
H=create_VideoHistory(VideoRecords)
print(H)
print(perform_Operations(H,'Operations1.csv'))