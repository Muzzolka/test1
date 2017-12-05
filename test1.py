from selenium import webdriver


browser = webdriver.Firefox()
browser.get("https://diabcontrol1.herokuapp.com/")
browser.find_element_by_id("id_username").send_keys("admin")
browser.find_element_by_id("id_password").send_keys("admin123")
browser.find_element_by_class_name("btn.btn-primary").click()
browser.find_element_by_link_text("My patients").click()

lista = [element.text for element in browser.find_elements_by_tag_name("td")]
print lista[0] + " " + lista[1] + " " + lista[2]
    #print emailtext + " " +fname.text + " " + lname.text

# emails = [email.text for email in browser.find_elements_by_class_name("email")]
# fnames = [fname.text for fname in browser.find_elements_by_class_name("fname")]
# lnames = [lname.text for lname in browser.find_elements_by_class_name("lname")]
# lists = zip(emails, fnames, lnames)
# for tupla in lists:
#         print tupla[0] + " " + tupla[1] + " " + tupla[2]

