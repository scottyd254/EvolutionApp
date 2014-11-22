class Ingredient < ActiveRecord::Base

	has_many :components
	belongs_to :user
end
