# from barcode import EAN13
# from barcode.writer import ImageWriter
#
# codigo_produtos = {
#     "Feijao" : "551746511111",
#     "Arroz" : "665789011111",
#     "Macarrao" : "665887111111",
#     "Azeite" : "998556211111"
# }
#
# for produto in codigo_produtos:
#     codigo = codigo_produtos[produto]
#     codigo_barra = EAN13(f'{codigo}', writer=ImageWriter())
#     codigo_barra.save(f'codigo_barra {produto}')

# import qrcode
#
# link_sites = {  # arquivos a serem lidos
#     "Instagram": "https://www.instagram.com/",
#     "Facebook": "https://www.facebook.com/",
#     "Youtube": "https://www.youtube.com/",
#     "Google": "https://www.google.com/",
# }
#
# for site in link_sites: # criação do qr_code
#     link = link_sites[site]
#     imagem_qr_code = qrcode.make(link)
#     imagem_qr_code.save(f"qr_code{site}.png")
