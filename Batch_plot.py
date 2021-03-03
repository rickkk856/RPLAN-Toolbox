import matplotlib.pyplot as plt

from rplan.floorplan import Floorplan
from rplan.align import align_fp_gt
from rplan.decorate import get_dw
from rplan.measure import compute_tf
from rplan.plot import get_figure,get_axes,plot_category,plot_boundary,plot_graph,plot_fp,plot_tf

# Put dataset in "./data" folder

from os import walk
mypath = './data/'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print("FILES LOADED ............",f)

lenght = len(f)

print("There will be loaded ",lenght," Images")

for f in f:
    file_path = ('./data/'+f)
    print("Loading Image From............",file_path)

    fp = Floorplan(file_path)
    img = fp.image    
    
    fp.boundary
    fp.category
    fp.instance
    fp.inside

    data = fp.to_dict()

    boxes_aligned, order, room_boundaries = align_fp_gt(data['boundary'],data['boxes'],data['types'],data['edges'])
    data['boxes_aligned'] = boxes_aligned
    data['order'] = order
    data['room_boundaries'] = room_boundaries

    doors,windows = get_dw(data)
    data['doors'] = doors
    data['windows'] = windows

    ## Activate the line of code of what type of image you want
    ## Images will be saved in "./output" folder with same filenames

    plt.axis('off')
    plot_category(fp.category) # raw image
    #plot_boundary(data['boundary']) # vector boundary
    #plot_graph(data['boundary'],data['boxes'],data['types'],data['edges']) # node graph
    #plot_fp(data['boundary'], data['boxes_aligned'][order], data['types'][order]) # vector floorplan
    #plot_fp(data['boundary'], data['boxes_aligned'][order], data['types'][order],data['doors'],data['windows']) # vector floorplan with doors and windows
    plt.savefig('./output/'+f, bbox_inches='tight')
    plt.close()
    
