Feature: Komputer wirtualny posiada dwa procesory

Scenario: Sprawdzenie ilosci procesorow
	Given Jestem  zalogowany na komputerze
	When sprawdzam ile procesorow posiada komputer
	Then Otrzymuje ilosc procesorow = 2
