# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141116031621) do

  create_table "ingredients", force: true do |t|
    t.string   "name"
    t.string   "unit"
    t.integer  "stock_max"
    t.integer  "stock_min_threshold"
    t.integer  "stock",               default: 0
    t.string   "external_id"
    t.string   "material_type"
    t.string   "active_or_excipient"
    t.text     "description"
    t.integer  "created_by"
    t.integer  "updated_by"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "products", force: true do |t|
    t.string   "name"
    t.text     "description"
    t.string   "package"
    t.integer  "average_weigth",              default: 0
    t.string   "unit"
    t.integer  "stock"
    t.integer  "number_of_blisters_per_box"
    t.integer  "number_of_units_per_blister"
    t.integer  "max_units_to_produce"
    t.string   "production_limited_by"
    t.string   "shape"
    t.integer  "created_by"
    t.integer  "updated_by"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

end
