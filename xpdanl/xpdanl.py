##############################################################################
#
# scans             by Billinge Group
#                   Simon J. L. Billinge sb2896@columbia.edu
#                   (c) 2016 trustees of Columbia University in the City of
#                        New York.
#                   All rights reserved
#
# File coded by:    Timothy Liu
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################


def plot_scan(header, field='pe1_image_light_field')
    ''' function to pull out and plot data from header specified
    
    Parameters
    ----------
    header : obj
        header object from DataBroker

    field : str
        name of filed you want to pull image from. default is pe1_image_lightfield
    
    Returns
    -------
    '''
    from dataportal import DataBroker as db
    from dataportal import get_events, get_table, get_images
    from tifffile import *
   
    # FIXME - make sure both dark and light image are in the same event 
    # FIXME - need a proper exception handler when data missing
    event = get_events(header, fill=False)
    
    # assume tiff squashing already has been done, only two imgs in header
    imgs = np.array(get_images(header, field))
    imgs_size = np.size(imgs)
    if imgs_size >2:
        print('There is more than one dark image and one light image in last header')
        print('Please contact beamline scientist to make sure tiff squashing is implented properly')
        return
    
    # plot dark subtracted image
    # FIXME - confirm there are only two images, dark and light in one header
    plot_img = imgs[1]-imgs[0]
    plt.figure()
    plt.imshoe(plot_img)
    plt.show()
    

def save_tif(header, f_name=None, dark_correct=True):
    ''' function to save (dark corrected) tiff
    
    Parameters
    ----------
    header : obj
        header object from DataBroker
    
    f_name : str
        file name to this tiff

    dark_correct : bool
        option to apply dark correction

    
    Returns
    -------
    
    '''
    if type(list(header))[1] == str:
        header_list = list()
        header_list.append(header)
    else:
        header_list = header

    if not f_name:
        # FIXME - use metadata in header
        print('use metadata from header')

    if dark_correct:
        # FIXME - perfom dark correction
        print('corect data with dark images')

    for header in header_list:
        prinr('Plotting and saving your data ....')
        # FIXME - using tiff exporter or tifffile ?
            
