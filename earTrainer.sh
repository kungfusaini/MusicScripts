#!/bin/sh
exec scala "$0" "$@"
!#
args.foreach(println)
import scala.util.Random
val random = new Random


val intervals = List("Major 2nd","Minor 2nd","Major 3rd","Minor 3rd","Perfect 4th","Tritone","Perfect 5th","Minor 6th","Major 6th","Minor 7th","Major 7th","Octave")
val unknown_intervals = List("Tritone","Minor 6th","Minor 7th")

//gives known intervals
val known = intervals.filter(!unknown_intervals.contains(_))


println()
println("Interval: " + known(random.nextInt(known.length)))
println()

