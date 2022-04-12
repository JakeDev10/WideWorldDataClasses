from dataclasses import dataclass, field

@dataclass
class Order:
    def __gt__(self, other):
        return self.OrderID > other.OrderID

    def __ge__(self, other):
        return self.OrderID >= other.OrderID

    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: str
    ExpectedDeliveryDate: str
    CustomerPurchaseOrderNumber: int
    IsUndersupplyBackordered: int
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: str
    LastEditedBy: int
    LastEditedWhen: str

@dataclass
class Invoice:
    def __gt__(self, other):
        return self.InvoiceID > other.InvoiceID

    def __ge__(self, other):
        return self.InvoiceID >= other.InvoiceID

    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: str
    CustomerPurchaseOrderNumber: int
    IsCreditNote: int
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: int
    RunPosition: int
    ReturnedDeliveryData: dict
    ComfirmedDeliveryTime: str
    ConfirmedRecievedBy: str
    LastEditedBy: int
    LastEditedWhen: str

@dataclass
class Customer:
    CustomerID: int
    CustomerName: str
    BillToCustomerID: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: int
    AccountOpenedDate: str
    StandardDiscountPercentage: float
    IsStatementSent: int
    IsOnCreditHold: int
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: int
    RunPosition: int
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: int
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: int
    LastEditedBy: int
    ValidFrom: str
    ValidTo: str

