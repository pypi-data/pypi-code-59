import os
import panel as pn
import numpy as np # used for the arrays and other mathematical operations
import astropy.io.fits as pyfits # used to handle fits files
import matplotlib.pyplot as plt # used for making plots
from matplotlib.figure import Figure
from ppxf.ppxf import ppxf
import ppxf.ppxf_util as util
pn.extension()


class Cube:
    """
    A class used to represent Integrated Field Spectrums that have a 'cube' shape.


    Attributes
    ----------
    header : Header object (Astropy)
        A formatted table that contains the corresponding header for this scientific data.
    
    data : numpy array
        A 3d numpy array that stores the scientific data.
    
    trimmed_data : numpy array
        A 3d numpy array that stores the trimmed scientific data, used for analyzing.
    
    wavelength_range : numpy array
        An array with only two values: the wavelengths that correspond to the first
        and last frames.
    
    wavelengths : numpy array
        An array with all the wavelengths corresponding to all the frames in the cube.
    
    nframes : int
        The number of frames contained in the data.

    Methods
    -------
    trimData(s1, e1, s2, e2)
        Sets the trimmed_data with the limits for the first axis being s1 and e1, 
        and the limits for the second axis being s2 and e2.
    
    displayFrameStatic(frame_number, needs_grid=False)
        Method used to display a specific frame. It gives an option to add a grid 
        to the plot.
    
    displayFrameInteractive(frame_number, needs_grid, s1, e1, s2, e2)
        Method used to display a specific frame with a specific trim, with the 
        possibility of adding a grid. This method is used internally by this class 
        and is not intended for the user. The user should instead use the 
        displayFrameStatic method.
    
    interactiveDataDisplay()
        Method used to interactevely explore the raw data. It allows to visualize 
        different frames as well as trim the scientific data in an interactive manner.


    """
    
    def __init__(self, file_name):
        """
        Parameters
        ----------
        file_name : str
            String that contains the file path for the .fits that will be used 
            to instantiate this Cube object.
        """


        # Open the .fits, get the data and the header, close the file
        cube_fits = pyfits.open(file_name)
        self.data = cube_fits[0].data
        self.header = cube_fits[0].header
        cube_fits.close()
        
        # Create other class variables based on the data
        # number of frames
        self.nframes = int(max(self.data.shape))
        # a copy of the data to be trimmed
        self.trimmed_data = self.data.copy()
        
        # the wavelength range
        # obtain relevant values from FITS header
        CRVAL3 = self.header["CRVAL3"]
        CRPIX3 = self.header["CRPIX3"]
        CD3_3 = self.header["CD3_3"]

        self.wavelength_range = (CRVAL3 - CRPIX3 * CD3_3) + np.array([0.,CD3_3*self.nframes])
        
        # the wavelengths
        self.wavelengths = np.linspace(self.wavelength_range[0], self.wavelength_range[1], self.nframes)
        

        #### TODO: ADD THE LAMRANGE HERE, AND ADD ALSO A METHOD SETLAMRANGE

        
    def trimData(self, s1, e1, s2, e2):
        """Sets the class variable trimmed_data with the parameters provided 
        by the user.

        Parameters
        ----------
        s1 : int
            The lower limit for the first axis.
        e1 : int
            The upper limit for the first axis.
        s2 : int
            The lower limit for the second axis.
        e2 : int
            The upper limit for the second axis.

        """
        self.trimmed_data = self.data[:, s1:e1, s2:e2].copy()

        
    def displayFrameStatic(self, frame_number, needs_grid=False):
        """Displays a static single frame from the data.

        Parameters
        ----------
        frame_number : int
            Index of the frame that will be displayed.
        needs_grid : boolean, optional
            When set to True, a grid is added on top of the plot.

        """

        #### TODO: change this to purely be plt.
        fig, ax = plt.subplots(figsize = (8,8))
        ax.set_xlabel('Pixel Number')
        ax.set_ylabel('Pixel Number')
        ax.set_title('Frame Displayer')
        im = ax.imshow(self.data[frame_number,:,:], cmap='gray')
        plt.colorbar(im)
        
        if needs_grid:
            plt.grid()

        plt.show() 


    def displayFrameInteractive(self, frame_number, needs_grid, s1, e1, s2, e2):
        """Used to display a specific frame with a specific trim, with the 
        possibility of adding a grid. This method is used internally by this class
        and is not intended for the user. 

        The user should instead use the displayFrameStatic method.

        Parameters
        ----------
        frame_number : int
            Index of the frame that will be displayed.
        needs_grid : boolean
            When set to True, a grid is added on top of the plot.
        s1 : int
            The lower limit for the first axis.
        e1 : int
            The upper limit for the first axis.
        s2 : int
            The lower limit for the second axis.
        e2 : int
            The upper limit for the second axis.

        Returns
        -------
        fig : matplotlib Figure
            Figure that contains the frame within the desired limits that 
            is going to be displayed.


        """

        # Create a figure and an axis objects with a square shape.
        fig, ax = plt.subplots(figsize = (8,8))

        # Customize the plot
        ax.set_xlabel('Pixel Number')
        ax.set_ylabel('Pixel Number')
        ax.set_title('Frame Displayer')
        
        # set the data to be displayed
        im = ax.imshow(self.data[frame_number, s1:e1, s2:e2], cmap='gray')

        # Add a colorbar
        plt.colorbar(im)
        
        # Add a grid if needed
        if needs_grid:
            plt.grid()

        # return the figure
        return fig
    
    def interactiveDataDisplay(self):
        """Displays a dashboard that can be used to interactively explore 
        the raw data and trim it.

        """
        
        # Create all the widgets used
        
        # First we have an Int Slider for the frame number being displayed
        frame_number_w = pn.widgets.IntSlider(name='Frame', start=0, 
                                              end=self.nframes-1, 
                                              step=1, value=0)
        frame_number_w.bar_color = '#59C1DD'
        
        
        # We have a Checkbox to display a grid on top of the meshgrid
        needs_grid_w = pn.widgets.Checkbox(name='Display Grid')
        
        
        # Now we have four widgets used to set the start and end indexes for both axes
        # lower limit of first axis
        l1_number1_w = pn.widgets.IntSlider(name="First Axis' start", start=0, 
                                            end=self.data.shape[1]-1, 
                                            step=1, value=0)

        l1_number1_w.bar_color = '#59C1DD'
        
        # upper limit of first axis
        l1_number2_w = pn.widgets.IntSlider(name="First Axis' end", start=0, 
                                            end=self.data.shape[1]-1, 
                                            step=1, value=self.data.shape[1]-1)

        l1_number2_w.bar_color = '#59C1DD'
        
        # lower limit of second axis
        l2_number1_w = pn.widgets.IntSlider(name="Second Axis' start", start=0, 
                                            end=self.data.shape[2]-1, 
                                            step=1, value=0)
        
        l2_number1_w.bar_color = '#59C1DD'
        
        # upper limit of second axis
        l2_number2_w = pn.widgets.IntSlider(name="Second Axis' end", start=0, 
                                            end=self.data.shape[2]-1, 
                                            step=1, value=self.data.shape[2]-1)

        l2_number2_w.bar_color = '#59C1DD'
        
        # dimensions of the trimmed cube
        dim_txt_w = pn.widgets.StaticText(value=f"Dimensions of Trimmed Data: ({self.trimmed_data.shape[0]}, {self.trimmed_data.shape[1]}, {self.trimmed_data.shape[2]})")
        
        # dimensions of the trimmed cube
        wave_txt_w = pn.widgets.StaticText(value=f"Wavelength: {self.wavelengths[frame_number_w.value]}")
        
        
        # trim button
        trim_button_w = pn.widgets.Button(name='Trim Data', button_type='primary')
        
        
        # Now we define the reactive funtion for the visualization and the funtion that trims the data
        def internal_trim_data(event):
            
            # Trim the data
            self.trimmed_data = self.data[:, l1_number1_w.value:l1_number2_w.value, l2_number1_w.value:l2_number2_w.value]
            
            # Update the static text
            dim_txt_w.value = f"Dimensions of Trimmed Data: ({self.trimmed_data.shape[0]}, {self.trimmed_data.shape[1]}, {self.trimmed_data.shape[2]})"
            
            
            
        
        @pn.depends(frame_number_w, needs_grid_w, l1_number1_w, l1_number2_w, l2_number1_w, l2_number2_w)
        def reactive_frames(frame_number, needs_grid, s1, e1, s2, e2):
            
            plt.close()
            
            # Update the max and min values for the trimming int sliders
            l1_number1_w.end = l1_number2_w.value - 1
            l1_number2_w.start = l1_number1_w.value + 1
            
            l2_number1_w.end = l2_number2_w.value - 1
            l2_number2_w.start = l2_number1_w.value + 1
            
            # Update the wavelength value
            wave_txt_w.value = f"Wavelength: {self.wavelengths[frame_number_w.value]}"
            
            
            return self.displayFrameInteractive(frame_number, needs_grid, s1, e1, s2, e2)

        
        # adding the trim function to the trim button
        trim_button_w.on_click(internal_trim_data)
        
        # create the dashboard
        self.data_display = pn.Row(reactive_frames, 
                                   pn.Column('<br>\n# Interactive Data Display',
                                             frame_number_w,
                                             needs_grid_w,
                                             wave_txt_w,
                                             dim_txt_w,
                                             '<br>\n### Change the start and end positions of both axes',
                                             l1_number1_w,
                                             l1_number2_w,
                                             l2_number1_w,
                                             l2_number2_w,
                                             trim_button_w))
        
        # Display the dashboard
        self.data_display.show()




import os
import panel as pn
import numpy as np # used for the arrays and other mathematical operations
import astropy.io.fits as pyfits # used to handle fits files
import matplotlib.pyplot as plt # used for making plots
from matplotlib.figure import Figure
from ppxf.ppxf import ppxf
import ppxf.ppxf_util as util
pn.extension()

class Assistant:
    """
    A class used to make the application of PPxF easier.


    Attributes
    ----------
    cube : Cube object (from this package)
        A cube that represents the data that will be processed.
    
    templates_directory : String
        A String that represents the absolute path where the templates are stored.
    
    templates_names : list
        A list with all the names of the templates being used.
    
    templates : dict
        A dictionary of the templates that are to be used.
    
    ntemplates: int
        The total number of templates that are to be used.
    
    output_directory : String
        A String that represents the absolute path where the results are to be
        saved at.
    
    results_ppxf : list
        A list that contains the results after having used PPxF in the cube


    Methods
    -------
    setOutputDirectory(output_directory)
        Sets the output directory.
    
    apply_ppxf(self, galnoise, FWHM_gal, FWHM_tem, z, moments, plot=False, directory_plots='')
        Applies the PPxF method to the trimmed data of the cube
    
    createResultsFile(self, filename='results.txt')
        This is saves the results in a tab separated file in the output directory.
        
    """
    
    def __init__(self, cube, templates_directory):
        """
        Parameters
        ----------
        cube : Cube object (from this package)
            A Cube object that represents the data that will be processed.
        templates_directory : String
            A String that represents the absolute path where the templates 
            are stored.
        """
        
        # the cube that this assistant will analize
        self.cube = cube
        # the directory where the templates are being stored
        self.templates_directory = templates_directory
        # the directory where the results are exported to
        self.output_directory = None
        
        # get the list of templates' names
        # first, get the list of template names
        self.templates_names = []

        for root, dirs, files in os.walk(self.templates_directory):
            for file in files:
                if file.endswith('.fits'):
                    self.templates_names.append(file)
        
        # the total number of templates
        self.ntemplates = len(self.templates_names)
        
        # the list that will contain the results
        self.results_ppxf = []
        
        # create empty dictionary
        self.templates = {}

        # populate the dictionary using the name of the templates as keys and a list of header, data for values
        for name in self.templates_names:
            # Open the .fits, get the data and the header, close the file
            template_fits = pyfits.open(self.templates_directory + name)
            template_data = template_fits[0].data
            template_header = template_fits[0].header
            template_fits.close()
            
            self.templates[name] = (template_header, template_data)

        
    def setOutputDirectory(self, output_directory):
        """Sets the class variable output_directory.

        Parameters
        ----------
        output_directory : String
            String of the absolute path where the results are to be exported to.
        """
        
        self.output_directory = output_directory
        

    def apply_ppxf(self, galnoise, FWHM_gal, FWHM_tem, z, moments, plot=False, directory_plots=''):
        """This is the method that uses the PPxF package and applies it to the trimmed
        data. It saves the results in the class variable 'results_ppxf'. It also has the
        possibility of saving the plots that it produces.

        Parameters
        ----------
        galnoise : float
            Noise in the galaxy's data.
        FWHM_gal : float
            Full width-half maximum of the galaxy.
        FWHM_tem : float
            Full width-half maximum of the templates.
        z : float
            The galaxy's redshift.
        moments : int
            The number of moments that should be used with PPxF.
        plot : boolean, optional
            Boolean to determine if the plots should be saved.
        directory_plots :  String
            String that represents the absolute path where the plots are 
            to be saved at.

        """
        
        # make sure that the list of results is empty
        self.results_ppxf = []

        temp_header, ssp = self.templates[self.templates_names[0]]

        CRVAL1h3 = temp_header["CRVAL1"]
        CRPIX1h3 = temp_header["CRPIX1"]
        CDELT1h3 = temp_header["CDELT1"]
        NAXIS1h3 = temp_header["NAXIS1"]
        
        # calculate the wavelenght range from the templates
        lamRange2 = (CRVAL1h3 - CRPIX1h3 * CDELT1h3) + np.array([0.,(CDELT1h3 * NAXIS1h3 - 1.0)])
        
        # speed of light
        c = 299792.458
        
        # Initial estimate of the galaxy's velocity in km/s
        vel = c * z
        
        # I NEED TO UNDERSTAND WHAT THE FOLLOWING TWO LINES MEAN
        goodPixels = np.arange(1150,1820) #(1150,1820) #[1150,1820] or perhaps an np.arange(1150,1820)

        start = [vel, 120.]
        
        # The current pixel being worked on
        number_of_pixel = 1

        ### Start nested loop
        for i in np.arange(self.cube.trimmed_data.shape[1]):

            for j in np.arange(self.cube.trimmed_data.shape[2]):
                
                # the spectrum corresponding to these pixel coordinates
                spec = self.cube.trimmed_data[:,i,j]

                galaxy, logLam1, velscale = util.log_rebin(self.cube.wavelength_range, spec)

                galaxy = galaxy/np.median(galaxy) # Normalizing the spectrum
                noise = galaxy*0 + galnoise # Assuming constant noise per pixel here

                sspNew, logLam2, velscale = util.log_rebin(lamRange2, ssp, velscale=velscale)

                templates = np.zeros((sspNew.shape[0], self.ntemplates))

                FWHM_dif = np.sqrt((FWHM_gal**2 - FWHM_tem**2))

                sigma = FWHM_dif/2.355/CDELT1h3

                #list_of_templates_names = list(templates_dictionary.keys())

                k = 0

                while k < self.ntemplates:
                    h3, ssp = self.templates[self.templates_names[k]]
                    ssp = util.gaussian_filter1d(ssp, sigma)  # perform convolution with variable
                    sspNew = util.log_rebin(lamRange2, ssp, velscale=velscale)[0]
                    templates[:, k] = sspNew/np.median(sspNew)
                    k += 1

                dv = (logLam2[0]-logLam1[0])*c # km/s

                pp = ppxf(templates, galaxy, noise, velscale, start,
                          goodpixels=goodPixels, plot=False, moments=moments, 
                          degree=4, mdegree = 0, vsyst=dv)

                self.results_ppxf.append(pp)

                if plot:
                    plt.rcParams['figure.figsize'] = (32,20)
                    myplt = pp.plot()
                    plt.savefig(directory_plots + str(number_of_pixel) + ".pdf")
                    plt.clf()
                    number_of_pixel += 1
    
    
    def createResultsFile(self, filename='results.txt'):
        """This is saves the results in a tab separated file in the output directory.

        Parameters
        ----------
        filename : String, optional
            String that represents the name that the output file will have.

        """
    
        # first element in the results
        first_element = self.results_ppxf[0]

        # length of a row
        length_of_row = (2*len(first_element.sol))+1

        # length of solution
        length_of_sol = len(first_element.sol)

        # make costume size. Twice the length of the sol (value and error) and one for chi^2
        results_np_arr = np.zeros(length_of_row) 

        # add the remaining moments
        for h in np.arange(length_of_sol):
            # current h
            results_np_arr[h*2] = first_element.sol[h]  
            # error of current h, defined to be = eroor_of_h * sqrt(chi^2)
            results_np_arr[h*2 + 1] = first_element.error[h]*np.sqrt(first_element.chi2)             

        # add chi^2
        results_np_arr[-1] = first_element.chi2        

        for element in self.results_ppxf[1:]:
            new_line = np.zeros(length_of_row)

            # add the remaining moments
            for h in np.arange(length_of_sol):
                # current h
                new_line[h*2] = element.sol[h]
                # error of current h, defined to be = eroor_of_h * sqrt(chi^2)
                new_line[h*2 + 1] = element.error[h]*np.sqrt(element.chi2)                    

            # add chi^2
            new_line[-1] = element.chi2         

            # stack the new line
            results_np_arr = np.vstack((results_np_arr, new_line))

        # create the header for the txt file
        header = 'V\t        Verr\t        Sigma\t        Sigerr'

        for i in np.arange(3,length_of_sol+1):
            header += '\t        H' + str(i) + '\t        H' + str(i) + 'err'

        header += '\t        Chi^2'

        np.savetxt(fname=self.output_directory+filename, 
                   X=results_np_arr, 
                   header=header, delimiter='\t', fmt='%f')



