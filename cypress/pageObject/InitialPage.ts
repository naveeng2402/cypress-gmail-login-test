class InitialPage {
  navigate() {
    cy.visit("https://accounts.google.com/signup");
  }

  enterFirstName(firstName: string) {
    if (firstName != "") {
      cy.get("#firstName").clear().type(firstName);
    }
    return this;
  }

  enterLastName(lastName: string) {
    if (lastName != "") {
      cy.get("#lastName").clear().type(lastName);
    }
    return this;
  }

  enterUserName(userName: string) {
    if (userName != "") {
      cy.get("#username").clear().type(userName);
    }
    return this;
  }

  enterPassword(password: string) {
    if (password != "") {
      cy.get("[name='Passwd']").clear().type(password);
    }
  }

  confirmPassword(password: string) {
    if (password != "") {
      cy.get("[name='ConfirmPasswd']").clear().type(password);
    }
  }

  moveNext() {
    cy.contains("Next").click();
  }

  checkNameError(err: string) {
    cy.xpath(
      "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span"
    ).should("contain.text", err);
  }

  checkUserNameError(err: string) {
    cy.xpath(
      "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div"
    ).should("contain.text", err);
  }

  checkPasswordError(err: string) {
    cy.xpath(
      "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div[2]/span"
    ).should("contain.text", err);
  }
}

export default InitialPage;
