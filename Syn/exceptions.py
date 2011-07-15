# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

class SynException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class SynDirectoryFailure(SynException):
	pass

class SynFormatException(SynException):
	pass

class ArchiveNotFoundException(SynException):
	pass

class InvalidJSONException(SynException):
	pass

class InvalidArchiveException(SynException):
	pass

class NotAnArchiveException(SynException):
	pass

class FileNotPresentException(SynException):
	pass

class BuildFailureException(SynException):
	pass

class MutexException(SynException):
	pass

class PackageNotFoundException(SynException):
	pass

class ConflictException(SynException):
	pass

class PackageInstalledException(SynException):
	pass

class PackageNotinstalledException(SynException):
	pass

class PackageUninstalledException(PackageNotinstalledException):
	pass

