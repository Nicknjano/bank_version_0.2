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
    #     self.submitTransactionButton.clicked.connect(self.handle_submit_transaction_button)
    #     QtCore.QMetaObject.connectSlotsByName(DashboardWindow)

    # mode = ''

    # def handle_transaction_clear(self):
    #     '''handles clear button on transaction page'''
    #     self.senderUserAccountField.clear()
    #     self.amountDoubleSpinBox.setValue(0.0)
    #     self.recepientAccountField.clear()
    #     self.sourceFundsComboBox.setCurrentIndex(0)
    #     self.transactorPINField.clear()
    #     self.transactionFeeLabel.clear()
    #     self.transactionFeeLabel.hide()
    #     self.successTransactionLabel.clear()

    # def handle_transfer_button(self):
    #     '''handles transfer button on transaction page'''
    #     self.mode = 'transfer'
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.recepientAccountLabel.show()
    #     self.recepientAccountField.show()
    #     self.sourceOfFundsLabel.show()
    #     self.sourceFundsComboBox.show()
    #     self.transactorPINField.show()
    #     self.transactionFeeLabel.show()
    #     self.transactionFeeLabel.hide()
    #     self.successTransactionLabel.hide()

    #     return self.mode

    # def handle_withdraw_button(self):
    #     '''handles withdraw button on transaction page'''
    #     self.mode = 'withdraw'
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.successTransactionLabel.hide()
    #     self.recepientAccountField.hide()
    #     self.sourceFundsComboBox.hide()
    #     self.transactorPINField.show()
    #     self.transactionFeeLabel.show()
    #     self.sourceOfFundsLabel.hide()
    #     self.recepientAccountLabel.hide()
    #     self.transactionFeeLabel.hide()

    #     return self.mode

    # def handle_deposit_button(self):
    #     '''handles deposit button on transaction page'''
    #     self.mode = 'deposit'
    #     self.senderUserAccountField.show()
    #     self.amountDoubleSpinBox.show()
    #     self.successTransactionLabel.hide()
    #     self.recepientAccountField.hide()
    #     self.sourceFundsComboBox.hide()
    #     self.transactorPINField.show()
    #     self.sourceOfFundsLabel.hide()
    #     self.recepientAccountField.hide()
    #     self.transactionFeeLabel.show()
    #     self.transactionFeeLabel.hide()

    #     return self.mode

    # def handle_submit_transaction_button(self):
    #     '''performs the submit action based on the current transaction mode'''
    #     if self.mode == 'transfer':
    #         pass
    #     elif self.mode == 'withdraw':
    #         pass
    #     elif self.mode == 'deposit':
    #         customer_id = self.senderUserAccountField.text()
    #         print(customer_id)
    #         amount = self.amountDoubleSpinBox.value()
    #         try:
    #             database.deposit(customer_id,amount)
    #             self.successTransactionLabel.setStyleSheet("color:rgb(0,255,0)")
    #             self.successTransactionLabel.show()
    #             self.successTransactionLabel.setText('Transaction Successful !!!')
    #         except:
    #             self.successTransactionLabel.setStyleSheet("color:rgb(255,0,0)")
    #             self.successTransactionLabel.show()
    #             self.successTransactionLabel.setText('OOPS Something Went Wrong...')
    #     else:
    #         self.successTransactionLabel.setStyleSheet("color:rgb(255,0,0)")
    #         self.successTransactionLabel.show()
    #         self.successTransactionLabel.setText('Please choose between ( transfer, deposit and withdraw ) !!!')
