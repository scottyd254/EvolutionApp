class Product < ActiveRecord::Base
	

  has_many :components
  has_many :calculates
end
