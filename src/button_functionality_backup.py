# """This file contains a copy of the functions written to handle some of the buttons"""
    #     self.retranslateUi(DashboardWindow)
    #     self.stackedWidget.setCurrentIndex(0)
    #     self.logoutButton.clicked.connect(DashboardWindow.close) # type: ignore
    #     self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) # type: ignore
    #     self.transactionsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) # type: ignore
    #     self.manageAdminsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3)) # type: ignore
    #     self.manageCustomersButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2)) # type: ignore
    #     self.mainDashboardTransactionButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    #     self.mainDashboardCustomerManagementButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
    #     self.mainDashboardAdminManagementButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
    #     self.clearTransactionButton.clicked.connect(self.handle_transaction_clear)
    #     self.transferButton.clicked.connect(self.handle_transfer_button)
    #     self.withdrawButton.clicked.connect(self.handle_withdraw_button)
    #     self.depositButton.clicked.connect(self.handle_deposit_button)
    #     QtCore.QMetaObject.connectSlotsByName(DashboardWindow)

    # def handle_transaction_clear(self):
    #     self.senderUserAccountField.clear()
    #     self.amountDoubleSpinBox.setValue(0.0)
    #     self.recepientAccountField.clear()
    #     self.sourceFundsComboBox.setCurrentIndex(0)
    #     self.transactorPINField.clear()
    #     self.transactionFeeLabel.clear()
    #     self.transactionFeeLabel.hide()
    #     self.successTransactionLabel.clear()

    # def handle_transfer_button(self):
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.recepientAccountLabel.show()
    #     self.recepientAccountField.show()
    #     self.sourceOfFundsLabel.show()
    #     self.sourceFundsComboBox.show()
    #     self.transactorPINField.show()
    #     self.transactionFeeLabel.show()
    #     self.successTransactionLabel.show()
    #     self.transactionFeeLabel.hide()

    # def handle_withdraw_button(self):
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.recepientAccountField.hide()
    #     self.sourceFundsComboBox.hide()
    #     self.transactorPINField.show()
    #     self.transactionFeeLabel.show()
    #     self.successTransactionLabel.show()
    #     self.sourceOfFundsLabel.hide()
    #     self.recepientAccountLabel.hide()
    #     self.transactionFeeLabel.hide()

    # def handle_deposit_button(self):
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.recepientAccountField.hide()
    #     self.sourceFundsComboBox.hide()
    #     self.transactorPINField.show()
    #     self.recepientAccountField.hide()
    #     self.transactionFeeLabel.show()
    #     self.successTransactionLabel.show()
    #     self.transactionFeeLabel.hide()
