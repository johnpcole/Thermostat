from boilerswitch_component import boilerswitch_module as BoilerSwitch
from thermostat_component import thermostat_module as Thermostat
from scheduler_component import scheduler_module as Scheduler
from display_component import display_module as Display
from common_components.userinterface_framework import userinterface_module as GUI
from controls_component import controls_module as Controller
from common_components.clock_datatype import clock_module as Clock
from common_components.meteo_framework import meteo_module as Meteo


def runapplication():

	# ===============================================================================================================
	GUI.init()
	# ===============================================================================================================

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# Define objects used to drive application     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	boilerswitch = BoilerSwitch.createboilerswitch()
	thermostat = Thermostat.createthermostat()
	scheduler = Scheduler.createscheduler()
	controls = Controller.createcontroller()
	display = Display.createdisplay(controls)

	tt = Clock.getnow().getvalue() - 100
	ss = 3
	scheduler.addscheduleditem(Clock.createastime(0, 10, tt), ss)
	scheduler.addscheduleditem(Clock.createastime(0, 50, tt), ss + 2)
	scheduler.addscheduleditem(Clock.createastime(0, 90, tt), ss + 4)
	scheduler.addscheduleditem(Clock.createastime(0, 130, tt), ss + 6)
	scheduler.addscheduleditem(Clock.createastime(0, 170, tt), ss + 8)
	scheduler.addscheduleditem(Clock.createastime(0, 210, tt), ss + 10)
	scheduler.addscheduleditem(Clock.createastime(0, 260, tt), ss + 12)
	scheduler.addscheduleditem(Clock.createastime(0, 310, tt), ss + 14)
	scheduler.addscheduleditem(Clock.createastime(0, 360, tt), ss + 16)
	scheduler.addscheduleditem(Clock.createastime(0, 410, tt), ss + 18)
	scheduler.addscheduleditem(Clock.createastime(0, 460, tt), ss + 20)
	scheduler.addscheduleditem(Clock.createastime(0, 520, tt), ss + 22)
	scheduler.addscheduleditem(Clock.createastime(0, 580, tt), ss + 24)
	scheduler.addscheduleditem(Clock.createastime(0, 640, tt), 24)
	waiter = 0
	#field = Field.createfield()
	#enemyarmy = EnemyArmy.createarmy()
	#defenderarmy = DefenderArmy.createarmy(field)
	#game = Game.creategame()
	meteolocation = Meteo.createlocation("Bristol+(UK)", -2.570310, 51.497772, 0)
	print meteolocation.getsuntimes(1, 1, 2018)


	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# Paint field and Start level 1                 #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	#display.paintwholefield(field)

	# ===============================================================================================================
	# ===============================================================================================================

	while controls.getquitstate() == False:

		currenttime = Clock.getnow()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# Process user input and resulting events       #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# Process any input events (mouse clicks, mouse moves)
		controls.processinput(boilercontroller)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# User moves mouse over field or clicks field           #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		newboilerinstruction = scheduler.checkschedule(currenttime)
		if newboilerinstruction != -1000:
			thermostat.setdesiredtemperature(newboilerinstruction)
			#print "New Boiler Instruction", newboilerinstruction
		timephase = abs((currenttime.getvalue() % 300) - 150)
		thermostat.setcurrenttemperature(timephase / 5.0)
		waiter = waiter + 1
		if waiter > 100:
			waiter = 0
			thermostat.updatethermostatstatus()
			boilerswitch.setdesiredswitchstatus(thermostat.getstatus())
			boilerswitch.updateboilerstatus()
		# If the field is enabled, update the selection property on the field and defender army objects
		# If we are in add/upgrade mode, we DONT want to start changing the current selection!!!
		#if controls.updatefieldselectionlocation(field) == True:

			# Update field selection data
			#field.updateselection(controls)

			# Update defender selection data
			#defenderarmy.updateselection(controls)

			# Update control selection data
			#controls.updatefieldselectionmode(field, defenderarmy)

			# If the user has clicked on the field, put the game in the correct add or upgrade state
			# (User states intention to add defender to specific field location or upgrade existing defender)
			#controls.invokemanagedefender(game, defenderarmy)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# User completes add or upgrade a defender to the game  #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# If the user has added or upgraded a defender, update the defender army
		#coinstolose = defenderarmy.managedefender(controls)

		#if coinstolose > 0:

			# Take coins out of user's account, if necessary for any actions performed
			#game.spendcoins(coinstolose)

			# Reset add/upgrade defender mode
			#controls.cancelmanagedefender()

			# Add new defender footprint to the field, if a new defender was added to the army
			#field.adddefendertofield(controls)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# Process Defenders & Enemies, walking + combat #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# Only process defenders and enemies if the game is NOT paused
		#if controls.getprocesswavestate() == True:

			# Loop over all enemies in the collection
			#for currentenemy in enemyarmy.units:

				# Move each enemy along the path
				#crystalstolose = currentenemy.move(field)

				# Take crystals out of user's account, if necessary
				#game.losecrystals(crystalstolose)

			# Loop over all defenders in the collection
			#for currentdefender in defenderarmy.units:

				# Identify the target enemy for each defender
				#enemyarmy.identifytargetenemy(currentdefender)

				# Move each defender
				#currentdefender.move(field, enemyarmy)

				# Recharge defender's strike, and if ready and on top of enemy, discharge
				# If the strike is successful, follow up with enemy take hit and gain coins actions
				#if currentdefender.combatenemy(enemyarmy) == True:

					# Take health away from enemy(s), and if necessary, remove from game if dead
					#coinstogain = enemyarmy.takehit(currentdefender, defenderarmy)

					# Add coins to user's account, if necessary
					#game.gaincoins(coinstogain)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# If all crystals are gone, game over           #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# If the game is flagged as game over
		#if game.isgameover() == True:

			# Reset game/control variables & Update all button states to reflect new wave plaque
			#controls.startnextlevel()

			# Set wave to 0, will change to 1 next cycle
			#game.initialisegame()

			# Remove Enemies from army collection
			#enemyarmy.wipearmy()

			# Remove Defenders from army collection
			#defenderarmy.wipearmy()

			# Remove Defenders from field
			#field.wipedefendersfromfield()

		# Refresh Screen
		#if currenttime.getsecond() % 5 == 0:
		display.refreshscreen(currenttime, controls, scheduler, boilercontroller)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# Else, if all enemies dead, start next level   #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# If the game is NOT flagged as game over
		#else:

			# If all enemy units are dead
			#if enemyarmy.isanyonealive() == False:

				# If all defender units are positioned at their base coordinates
				#if defenderarmy.isanyoneawayfrombase() == False:

					# Pause game in "between waves" mode
					#controls.startnextlevel()

					# Start next level
					#game.startnextlevel()

					# Repopulate enemy army with new enemies for the next level
					#enemyarmy.populatearmy(game, field)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		# Refresh button states, display and maintain refresh rate  #
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

		# Refresh screen if all frames are required, or important frames if only some
		#display.refreshscreen(enemyarmy, defenderarmy, field, controls, game)

	# ===============================================================================================================
	GUI.quit()
	# ===============================================================================================================

