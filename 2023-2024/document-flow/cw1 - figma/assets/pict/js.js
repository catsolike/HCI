let imgs = document.getElementsByTagName("img")

async function downloadImage(
  imageSrc,
  nameOfDownload = 'my-image.png',
) {
  const response = await fetch(imageSrc);

  const blobImage = await response.blob();

  const href = URL.createObjectURL(blobImage);

  const anchorElement = document.createElement('a');
  anchorElement.href = href;
  anchorElement.download = nameOfDownload;

  document.body.appendChild(anchorElement);
  anchorElement.click();

  document.body.removeChild(anchorElement);
  window.URL.revokeObjectURL(href);
}


for (var x = 0; 0 < imgs.length; x ++){
    setTimeout(
        downloadImage(imgs[x].src), 3000
    );
}