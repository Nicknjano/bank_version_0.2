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
    #     self.customerManagementClearButton.clicked.connect(self.handle_customer_clear)
    #     self.viewCustomersButton.clicked.connect(self.handle_view_customers)
    #     self.createCustomerButton.clicked.connect(self.handle_create_customer)
    #     self.deleteCustomerButton.clicked.connect(self.handle_delete_customer)
    #     self.updateCustomerButton.clicked.connect(self.handle_update_customer)
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
    #     self.handle_transaction_clear()
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
    #     self.handle_transaction_clear()
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
    #     self.handle_transaction_clear()
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
    #         customer_id = self.senderUserAccountField.text()
    #         amount = self.amountDoubleSpinBox.value()
    #         funds_source = self.sourceFundsComboBox.currentText()
    #         recepient_id = self.recepientAccountField.text()
    #         if customer_id == '':
    #             self.transaction_error('User account can not be empty...')
    #             return
    #         if amount <= 0:
    #             self.transaction_error('Transfer amount must be grater than zero...')
    #             return
    #         if recepient_id == '':
    #             self.transaction_error('Recepient account can not be empty...')
    #             return
    #         if recepient_id == customer_id :
    #             self.transaction_error('Sender account can not be the same as Recepient account')
    #             return
    #         try:
    #             result = database.transfer(customer_id,recepient_id,funds_source,amount)
    #             if result == None:
    #                 balance = database.get_balance(customer_id)
    #                 self.transaction_success(f'Transfer Successful !!!\nNew account balance {balance}.')
    #             elif result == 1:
    #                 self.transaction_error('Insufficient account balance')
    #             elif result == 2:
    #                 self.transaction_error('Please check the accounts')
    #             else:
    #                 self.transaction_error('OOPS Something went wrong on our side')
                    
    #         except:
    #             self.transaction_error('Wrong accounts entered ')


    #     elif self.mode == 'withdraw':
    #         customer_id = self.senderUserAccountField.text()
    #         amount = self.amountDoubleSpinBox.value()
    #         if customer_id == '':
    #             self.transaction_error('User account can not be empty...')
    #             return
    #         if amount <= 0:
    #             self.transaction_error('Withdraw amount must be grater than zero...')
    #             return
    #         try:
    #             result = database.withdraw(customer_id,amount)
    #             if result == None:
    #                 balance = database.get_balance(customer_id)
    #                 self.transaction_success(f'Withdraw Successful !!!\nNew account balance {balance}.')
    #             else:
    #                 self.transaction_error('Insufficient account balance')                    
    #         except:
    #             self.transaction_error('Wrong User account or PIN')
    #     elif self.mode == 'deposit':
    #         customer_id = self.senderUserAccountField.text()
    #         amount = self.amountDoubleSpinBox.value()
    #         if customer_id == '':
    #             self.transaction_error('User account can not be empty...')
    #             return
    #         if amount <= 0:
    #             self.transaction_error('Deposit amount must be grater than zero...')
    #             return
    #         try:
    #             database.deposit(customer_id,amount)
    #             balance = database.get_balance(customer_id)
    #             self.transaction_success(f'Deposit Successful !!!\nNew account balance {balance}.')
    #         except:
    #             self.transaction_error('Wrong User account or PIN')
    #     else:
    #         self.transaction_error('Please choose ( transfer, deposit or withdraw ) !!!')

    # def transaction_error(self,message):
    #     '''displays an error if a transaction doesnt go through'''
    #     self.successTransactionLabel.setStyleSheet("color:rgb(255,0,0)")
    #     self.successTransactionLabel.show()
    #     self.successTransactionLabel.setText(message)

    # def transaction_success(self,message):
    #     '''displays success message if a transactio goes through'''
    #     self.successTransactionLabel.setStyleSheet("color:rgb(0,255,0)")
    #     self.successTransactionLabel.show()
    #     self.successTransactionLabel.setText(message)

    # def handle_customer_clear(self):
    #     '''handles the clear button on the customer management page'''
    #     self.customerIdField.clear()
    #     self.customerFirstNameField.clear()
    #     self.customerSecondNameField.clear()
    #     self.customerLastNameField.clear()
    #     self.accountTypeComboBox.setCurrentIndex(0)
    #     self.accountBalanceDoubleSpinBox.setValue(0.0)
    #     self.updateCustomerStatusLabel.clear()

    # def handle_view_customers(self):
    #     pass
    #     # '''handles the view customer button on customer management page'''
    #     # from PyQt5.QtGui import QStandardItem, QStandardItemModel
    #     # self.handle_customer_clear()
    #     # customers = database.get_customers()
    #     # model = QStandardItemModel
    #     # model.setHorizontalHeaderLabels(["staff_number","password","first_name","second_name","last_name","position","status"])
    #     # self.customerListTreeView.setModel(model)

    #     # return model


    # def handle_create_customer(self):
    #     '''handles the create customer button on customer management page'''
    #     customer_id = self.customerIdField.text()
    #     first_name = self.customerFirstNameField.text()
    #     second_name = self.customerSecondNameField.text()
    #     last_name = self.customerLastNameField.text()
    #     account_type = self.accountTypeComboBox.currentText()
    #     account_balance = self.accountBalanceDoubleSpinBox.value()
    #     result = database.add_customer(customer_id,first_name,second_name,last_name,account_type,account_balance)
    #     if result == 1:
    #         self.update_customer_fail('Customer ID can not be empty...')
    #     elif result == 'customer exists':
    #         self.update_customer_fail('Customer arleady exists...')
    #     elif result == 2:
    #         self.update_customer_fail('OOPS Something went wrong...')
    #     else:
    #         self.handle_customer_clear()
    #         self.update_customer_success('Customer created successfully...')
            

    # def handle_delete_customer(self):
    #     '''handles the delete button of customer management page'''
    #     customer_id = self.customerIdField.text()
    #     result = database.get_customer(customer_id)
    #     if result == None:
    #         self.update_customer_fail('Customer does not exist...')
    #     else:
    #         other_result = database.delete_customer(customer_id)
    #         if other_result == None:
    #             self.handle_customer_clear()
    #             self.update_customer_success('Customer deleted successfully')               
    #         else:
    #             self.update_customer_fail('OOPS something went wrong...')

    # def handle_update_customer(self):
    #     '''handles the update button of the customer management page'''
    #     customer_id = self.customerIdField.text()
    #     first_name = self.customerFirstNameField.text()
    #     second_name = self.customerSecondNameField.text()
    #     last_name = self.customerLastNameField.text()
    #     account_type = self.accountTypeComboBox.currentText()
    #     account_balance = self.accountBalanceDoubleSpinBox.value()
    #     result = database.update_customer(customer_id,first_name,second_name,last_name,account_type,account_balance)
    #     if result == 1:
    #         self.update_customer_fail('Customer does not exist...')
    #     elif result == 2:
    #         self.update_customer_fail('OOPS Something went wrong...')
    #     else:
    #         self.handle_customer_clear()
    #         self.update_customer_success('Customer updated successfully...')

    # def update_customer_success(self,message):
    #     '''prints success message for successful customer update'''
    #     self.updateCustomerStatusLabel.setStyleSheet("color:rgb(0,255,0)")
    #     self.updateCustomerStatusLabel.setText(message)

    # def update_customer_fail(self,message):
    #     '''prints success message for successful customer update'''
    #     self.updateCustomerStatusLabel.setStyleSheet("color:rgb(255,0,0)")
    #     self.updateCustomerStatusLabel.setText(message)
