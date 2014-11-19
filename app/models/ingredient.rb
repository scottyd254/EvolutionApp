class Ingredient < ActiveRecord::Base

	has_many :components
end
