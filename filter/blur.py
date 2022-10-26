from PIL import Image, ImageFilter #Podemos usar, isso para desfocar uma imagem

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")

#incluimos uma biblioteca com import e aqui vamos os nomes Image e da biblioteca. ImageFilter PIL
#image e um objeto, objetos em python podem ter nao apenas valores, mas funcoes que podemos acessar com a . sinatxe, como com image.open. 