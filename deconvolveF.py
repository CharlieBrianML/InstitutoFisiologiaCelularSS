
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
from scipy import ndimage, signal
from flowdec import data as fd_data
from flowdec import restoration as fd_restoration
from skimage.exposure import rescale_intensity
import cv2
from fourier import TF2
from fourier import supFrecq2

# ===> Loading data
data = cv2.imread('Images/verdeactrojomiosinaazulsinapto20Hz1.png',0)   # image for deconvolution
img = cv2.imread('Deconvolutions/Deconvolve_verdeactro.png', 0) # image for fft
img2 = cv2.imread('Deconvolutions/Deconvolve_verdeactro2.png', 0) # image for fft
img3 = cv2.imread('Deconvolutions/Deconvolve_verdeactro3.png', 0) # image for fft
imgdeconv = cv2.imread('Deconvolutions/Deconvolve_verdeactro.png')
#plt.plot(np.arange(800*800),np.reshape(img,800*800),'o')
#plt.show()
#plt.imshow(data, cmap='gray')
#plt.show()

# ===> Deconvolution of data image
kernel = plt.imread('PSF/PSF_BW4.png')
print("La psf dim: ",kernel.shape)
#plt.plot(np.arange(800*800),np.reshape(kernel[:,:,1],800*800),'o')
#plt.show()
#plt.imshow(kernel, cmap='gray')
#plt.show()

iteration = 30
'''
algo = fd_restoration.RichardsonLucyDeconvolver(data.ndim).initialize()
res = algo.run(fd_data.Acquisition(data=data, kernel=kernel), niter=iteration).data
#plt.imshow(res, cmap='gray')
#plt.show()
'''

'''
for o in range(100):
	for i in range(800):
		for j in range(800):
			if(np.abs(f[i][j])==np.abs(k[i][j])):
				print("Hay una coincidencia")
			f[i][j]=f[i][j]-k[i][j]
'''		
'''	
for i in range(800):
	for j in range(800):
		if(np.abs(k[i][j])<0.1):
			if(np.abs(f[i][j])>0.1):
				f[i][j]=f[i][j]
			else:
				f[i][j]=0.0j
				print("Hay una coincidencia")
		else:
			f[i][j]=f[i][j]/500*k[i][j]

plt.figure(4)
plt.vlines(freq,0,np.reshape(np.abs(f),800*800))
plt.show()
'''
'''
print("La tranformada: ",f.shape)
fshift = np.fft.fftshift(f)
magnitude_spectrum_data = 20*np.log(np.abs(fshift))
# # ===> FFT of deconvoluted image
'''
imgF = TF2(data)
freqs = np.arange(500,2500)
print(freqs)
imgS = supFrecq2(imgF,freqs,0.0)
#fdeconvI = np.fft.ifft2(imgdeconv[:,:,1])

fI = rescale_intensity(np.abs(np.fft.ifft2(imgS)), in_range=(0, 255))
fI = (fI * 255).astype("uint8")

#fdeconvI = rescale_intensity(np.abs(f), in_range=(0, 255))
#fdeconvI = (fdeconvI * 255).astype("uint8")

cv2.imshow("Convolucion", data)
cv2.imshow("Deconvolution", fI)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

f = np.fft.fft2(res)
fshift = np.fft.fftshift(f)
magnitude_spectrum_res = 20*np.log(np.abs(fshift)+0.001)


data = rescale_intensity(data, in_range=(0, 255))
data = (data * 255).astype("uint8")
'''
#f = rescale_intensity(np.abs(f), in_range=(0, 255))
#f = (img * 255).astype("uint8")
'''
res = rescale_intensity(res, in_range=(0, 255))
res = (res * 255).astype("uint8")

magnitude_spectrum_data = rescale_intensity(magnitude_spectrum_data, in_range=(0, 255))
magnitude_spectrum_data = (magnitude_spectrum_data * 255).astype("uint8")
'''
'''
# ===> Showing the deconvolution
f1 = plt.figure(1)
plt.subplot(121), plt.imshow(data, cmap='gray')
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(res, cmap='gray')
plt.title('Deconvolution'), plt.xticks([]), plt.yticks([])
#plt.show()
'''
# # ===> Showing FFT original
#f2 = plt.figure(2)
#plt.subplot(121), plt.imshow(img, cmap='gray')
#plt.imshow(img, cmap='gray')
#plt.title('Original image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122), plt.imshow(np.abs(f), cmap='gray')
#plt.imshow(np.abs(f), cmap='gray')
#plt.title('FFT Original image'), plt.xticks([]), plt.yticks([])
#plt.show()
# # # ===> Showing FFT deconvolution
'''
cv2.imshow("Original", img)
cv2.imshow("Transformada", f)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
f3 = plt.figure(3)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum_res, cmap='gray')
plt.title('FFT deconvolution'), plt.xticks([]), plt.yticks([])

plt.show()  # uncomment to show the figures
'''
'''
f1.savefig('./output_images/deconvolution.pdf', bbox_inches='tight')
f2.savefig('./output_images/originalFFT.pdf', bbox_inches='tight')
f3.savefig('./output_images/deconvolutionFFT.pdf', bbox_inches='tight')

plt.imsave('./output_images/original.png', data, cmap='gray')
plt.imsave('./output_images/deconvolution.png', res, cmap='gray')
plt.imsave('./output_images/original_FFT.png', magnitude_spectrum_data, cmap='gray')
plt.imsave('./output_images/deconvolution_FFT.png', magnitude_spectrum_res, cmap='gray')
'''