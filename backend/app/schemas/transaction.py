from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from decimal import Decimal
from typing import Literal

class CategoryBase(BaseModel):
    name: str
    type: Literal["income", "expense"]

class CategoryCreate(CategoryBase):
    pass 

class CategoryOut(CategoryBase):
    id:int
    model_config = ConfigDict(from_attributes=True)

class TransactionBase(BaseModel):
    amount: Decimal

class TransactionCreate(BaseModel):
    amount: Decimal
    category_id: int

class TransactionOut(TransactionBase):
    id: int
    date: datetime
    category: CategoryOut
    model_config = ConfigDict(from_attributes=True)
        
class TransactionUpdate(BaseModel):
    # made optional so you can update one or both
    amount: Optional[Decimal] = None
    category_id: Optional[int] = None

class CategoryTotal(BaseModel):
    category:str
    total: Decimal

class GoalCreate(BaseModel):
    category_id: int
    weekly_budget: Decimal

class GoalUpdate(BaseModel):
    weekly_budget: Optional[Decimal] = None

# what the API returns after creating/listing/updating a goal
class GoalOut(BaseModel):
    id: int
    weekly_budget: Decimal
    category:CategoryOut
    model_config = ConfigDict(from_attributes=True)
        
class GoalProgress(BaseModel):
    category_id: int
    category_name:str
    spent: Decimal
    weekly_budget: Decimal
    pct_used: Decimal
    status: str



