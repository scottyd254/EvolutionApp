class Component < ActiveRecord::Base

  belongs_to :product
  belongs_to :ingredient
  belongs_to :user
end
