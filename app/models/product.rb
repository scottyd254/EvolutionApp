class Product < ActiveRecord::Base
	

  has_many :components
  has_many :calculates
  belongs_to :user, foreign_key: "created_by"
end
